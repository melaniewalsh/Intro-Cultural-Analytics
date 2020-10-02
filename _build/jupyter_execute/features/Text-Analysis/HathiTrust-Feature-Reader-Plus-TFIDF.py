# TF-IDF With HathiTrust Volumes

## Installation

!pip install htrc-feature-reader

## Download Extracted Features From The Command Line

Lost in the City

https://babel.hathitrust.org/cgi/pt?id=mdp.39015029970129

Download extracted features into my current directory

!htid2rsync mdp.39015029970129 | rsync --files-from - data.analytics.hathitrust.org::features-2020.03/ .

Download extracted features into new directory called "hathi-files"

!htid2rsync mdp.39015029970129 | rsync --files-from - data.analytics.hathitrust.org::features-2020.03/ hathi-files/

## Download Extracted Features With Python

from htrc_features import utils

utils.id_to_rsync('mdp.39015029970129')

## Download extracted features from the web

from htrc_features import Volume

volume = Volume("mdp.39015029970129")

volume

### Read in extracted features from file

from htrc_features import Volume

volume = Volume("hathi-files/mdp/31272/mdp.39015029970129.json.bz2")

volume

## Download Volume IDs From HathiTrust Collection

https://solr2.htrc.illinois.edu/solr-ef/?solr-key-q=17083A600227127535CCB993F515A8220&start=31&group-by-vol=0

!pip install htrc

James Baldwin HathiTrust collection that I created: https://babel.hathitrust.org/cgi/mb?a=listis;c=2098723708

from htrc import workset
volume_ids = workset.load_hathitrust_collection('https://babel.hathitrust.org/cgi/mb?a=listis;c=2098723708')

volume_ids

for hathi_id in volume_ids:
    vol = Volume(hathi_id)
    print(hathi_id, vol.title)

## Download Volume IDs From HathiTrust Workset

Make a Workset. Then Download volumes IDs.

volume_ids = pd.read_csv('James-Baldwin-Workset.csv')['id']

for hathi_id in volume_ids:
    vol = Volume(hathi_id)
    print(hathi_id, vol.title)

## Make Word Count DataFrame From All Volumes

import pandas as pd

all_tokens = []

for hathi_id in volume_ids:
    #Read in volume
    volume = Volume(hathi_id)
    
    #Make dataframe from token list -- do not include part of speech, sections, or case sensitivity
    token_df = volume.tokenlist(case=False, pos=False, drop_section=True)
    
    #Add book column
    token_df['book'] = volume.title
    
    #Add publication year column
    token_df['year'] = volume.year
    
    all_tokens.append(token_df)

baldwin_df = pd.concat(all_tokens)

Change from multi-level index to regular index with `reset_index()`

baldwin_df_flattened = baldwin_df.reset_index()

baldwin_df_flattened 

Summarize token counts for each book

baldwin_df_flattened.groupby(['book', 'year', 'lowercase'])[['count']].sum().reset_index()

word_frequency_df = baldwin_df_flattened.groupby(['book', 'year', 'lowercase'])[['count']].sum().reset_index()

## Remove Infrequent Words, Stopwords, & Punctuation

Remove words that appear less than 5 times in a book

word_frequency_df = word_frequency_df[word_frequency_df['count'] > 5]

Remove stopwords

STOPS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
         'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
         'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
         'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
         'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
         'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
         'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
         'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
         'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
         'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
         'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
         'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 've', 'll', 'amp', "!"]

word_frequency_df = word_frequency_df.drop(word_frequency_df[word_frequency_df['lowercase'].isin(STOPS)].index)

Remove punctuation

word_frequency_df = word_frequency_df.drop(word_frequency_df[word_frequency_df['lowercase'].str.contains('[^A-Za-z\s]', regex=True)].index)

word_frequency_df

## TFIDF

word_frequency_df = word_frequency_df.rename(columns={'lowercase': 'term','count': 'term_frequency'})

word_frequency_df

Calculate document frequency (in how many books in the collection does this term appear?)

document_frequency_df = (word_frequency_df.groupby(['book','term']).size().unstack(fill_value=0) > 0).sum().reset_index()

document_frequency_df = document_frequency_df.rename(columns={0:'document_frequency'})

word_frequency_df = word_frequency_df.merge(document_frequency_df)

word_frequency_df

Calculate total number of documents 

total_number_of_documents = baldwin_df_flattened['book'].nunique()

Calculate tfidf

from math import log

word_frequency_df['tfidf'] = word_frequency_df['term_frequency'] * (log(1 + total_number_of_documents)) /  (1+ word_frequency_df['document_frequency']) + 1

word_frequency_df['tfidf_normalized']=(word_frequency_df['tfidf'] - word_frequency_df['tfidf'].mean())/word_frequency_df['tfidf'].std()

word_frequency_df['tfidf_sklearnnormalized'] = sklearn.preprocessing.normalize(word_frequency_df[['tfidf']], axis=0, norm='l2')

Find top 15 words with highest tfidf scores for each book

word_frequency_df.sort_values(by=['book','tfidf_sklearnnormalized'], ascending=False).groupby(['book']).head(15)

word_frequency_df.sort_values(by='tfidf', ascending=False)[:100]

word_frequency_df.groupby(['book', 'lowercase'])[[ 'lowercase','tfidf']].sort_values(by='tfidf', ascending=False).nlargest(10)

pd.set_option("max_rows", 500)

word_frequency_df.groupby('book')[['tfidf', 'lowercase']].nlargest(10).reset_index()

word_frequency_df.groupby('book')[['tfidf', 'lowercase']].nlargest(10)

def pretty_plot_top_n(series, top_n=5, index_level=0):
    
    r = series.groupby(level=index_level).nlargest(top_n).reset_index(level=index_level, drop=True)
    #r.plot.bar()
    return r.to_frame()


pretty_plot_top_n(word_frequency_df['tfidf'])

word_frequency_df[word_frequency_df['tfidf'] = word_frequency_df.groupby('book')['tfidf'].nlargest(5).reset_index(drop=True)]

word_frequency_df.groupby('book')[['book','tfidf', 'lowercase']].reset_index().sort_values(by='tfidf')

word_frequency_df.sort_values(by=['book', 'tfidf'], ascending=False)[:100]

word_frequency_df.groupby(['book', 'lowercase']).nlargest()

inverse_document_frequency = (log(total_number_of_documents) / number_of_documents_with_term) + 1

term_frequency * inverse_document_frequency 



(word_frequency_df.groupby(['book','lowercase']).size().unstack(fill_value=0) > 0).groupby('book')

word_frequency_df

### Get Top n Words For Each Book

def calculate_document_frequency(token):
    if token

baldwin_df_flattened

def calculate_document_frequency(current_token):
    

for book, token in baldwin_df_flattened.groupby('book')['token']:
    #if token == 'black':
    print(book, token.values)

[x for x in baldwin_df_flattened.token.values if token in x]



len([x for x in df.tokens.values if token in x])) for token in tf.columns]

baldwin_df_flattened.groupby(['book','token']).size().unstack(fill_value=0)

(baldwin_df_flattened.groupby(['book','token']).size().unstack(fill_value=0) > 0).sum()

baldwin_df_flattened.groupby(['book', 'token']).count()

baldwin_df_flattened['doc_frequency'] = (baldwin_df_flattened.groupby(['book', 'token'])['token'].count() > 0).sum()
baldwin_df_flattened

(baldwin_df_flattened.groupby(['book', 'token'])['count'].sum() > 0).sum()

total_number_of_documents

baldwin_df_flattened['book'].nunique()

len(baldwin_df_flattened.groupby(['book', 'token'])[['book', 'token']].count() > 0)

from math import log

total_number_of_documents

baldwin_df_flattened.groupby(['book', 'token'])[['count']].sum()

term_frequency 

term_frequency = baldwin_df_flattened.groupby(['book', 'token'])[['count']].sum()

number_of_documents_with_term = (baldwin_df_flattened.groupby(['book','token']).size().unstack(fill_value=0) > 0).sum()

number_of_documents_with_term

inverse_document_frequency

inverse_document_frequency = (log(total_number_of_documents) / number_of_documents_with_term) + 1

term_frequency * inverse_document_frequency 

baldwin_df_flattened.groupby(['token'])[['count']].sum()

baldwin_df_flattened.groupby(['book', 'token'])[['count']].sum() / baldwin_df_flattened.groupby(['token'])[['count']].sum()

term_frequency = 30 ##number of times "pigeons" appears in "The Girl Who Raised Pigeons"
inverse_document_frequency = log(total_number_of_documents / number_of_documents_with_term) + 1

baldwin_df_flattened.groupby(['book', 'token'])[['count']].sum().groupby('book').to_numpy().shape

baldwin_df_flattened.groupby(['book', 'token'])[['count']].sum().groupby('book')['count'].nlargest(100).droplevel(0).reset_index()

baldwin_df.groupby(level=['token'], 'book')[['count']].sum().sort_values(by='count', ascending=False)[:100]

baldwin_df.groupby(level='token')[['count']].sum().sort_values(by='count', ascending=False)[:100]

baldwin_df.sort_values(by='count', ascending=False)

baldwin_df_flattened

baldwin_df_flattened.book.value_counts()

baldwin_df_flattened.groupby(['book', 'token'])[['count', 'book']].sum().sort_values(by=[ 'book', 'count'], ascending=False).nlargest(10, columns=[ 'count'])

https://babel.hathitrust.org/cgi/mb?a=listis;c=447365647

## Get Metadata

volume.title

volume.year

volume.page_count

volume.publisher

volume.handle_url

volume.parser.meta

All possible metadata categories

volume.parser.meta.keys()

## Work With Tokens

volume.tokenlist()

volume.tokenlist(page=False, section=None, pos=False)

import pandas as pd

pd.set_option("max_rows", 600)

lost_df = volume.tokenlist()

lost_df.columns

lost_df

lost_df.query('page == 41')

lost_df.query('token == "pigeon"')

volume.tokenlist()[:100]

lost_df_flattened = lost_df.reset_index()

lost_df_flattened[lost_df_flattened['token'] == "LIONS"]

lost_df_flattened[lost_df_flattened['token'] == "TRAIN"]

lost_df_flattened[lost_df_flattened['token'] == "DAY"]

lost_df_flattened[lost_df_flattened['page'] == 117]

lost_df_flattened.info()

def add_chapter_titles(page):
    if page >= 11 and page < 35:
        return "Ch1: The Girl Who Raised Pigeons"
    elif page >= 35 and page < 41:
        return "Ch2: The First Day"
    elif page >= 41 and page < 63:
        return "Ch3: The Night Rhonda Ferguson Was Killed"
    elif page >= 63 and page < 85:
        return "Ch4: Young Lions"
    elif page >= 85 and page < 113:
        return "Ch5: The Store"
    elif page >= 113 and page < 125:
        return "Ch6: An Orange Line Train to Ballston"
    elif page >= 125 and page < 149:
        return "Ch7: The Sunday Following Mother's Day"
    elif page >= 149 and page < 159:
        return "Ch8: Lost in the City"
    elif page >= 159 and page < 184:
        return "Ch9: His Mother's House"
    elif page >= 184 and page < 191:
        return "Ch10: A Butterfly on F Street"
    elif page >= 191 and page < 209:
        return "Ch11: Gospel"
    elif page >= 209 and page < 225:
        return "Ch12: A New Man"
    elif page >= 225 and page < 237:
        return "Ch13: A Dark Night"
    elif page >= 237:
        return "Ch14: Marie"

lost_df_flattened['chapter'] = lost_df_flattened['page'].apply(add_chapter_titles)

lost_df_flattened['chapter'].value_counts()

lost_df_flattened

from sklearn.feature_extraction.text import TfidfVectorizer
v = TfidfVectorizer()
x = v.fit_transform(df['sent'])

from sklearn.feature_extraction.text import TfidfVectorizer


from sklearn.feature_extraction.text import TfidfTransformer


tfidf_transformer = TfidfTransformer()

from numpy import log
def tfidf(x):
    return x * log(1+vol.page_count / x.count())

# Will take a few seconds to run, depending on your system
idf_scores = lost_df_flattened.groupby(level=["token"]).transform(tfidf)

lost_df.groupby(level=["token"]).count()

len(lost_df_flattened['chapter'].unique())

document_frequency = lost_df_flattened['chapter'].

def calculate_tfidf(term_frequency):
    return term_frequency * log(1+14 / term_frequency.count())

log(total_number_of_documents / number_of_documents_with_term) + 1

lost_df_flattened.groupby(['chapter', 'token'])['count'].count().transform(calculate_tfidf)['count']

lost_df.groupby(level=["token"]).count()

lost_df_flattened.groupby(['chapter', 'token']).count()

from numpy import log
def tfidf(x):
    return x * log(1+volume.page_count / x.count())



# Will take a few seconds to run, depending on your system
idf_scores = lost_df.groupby(level=["token"]).transform(tfidf)
idf_scores

tfidf_transformer.fit_transform(lost_df_flattened[['token', 'count']])

tfidf_vectorizer = TfidfVectorizer(stop_words='english')

tfidf_vectorizer.fit_transform(lost_df_flattened[])

lost_df_flattened['section'].value_counts()

lost_df_flattened[lost_df_flattened['section'] == 'header']

lost_df.sort_values(by='count', ascending=False)

lost_df = volume.tokenlist()

lost_df = volume.tokenlist(pages=False, pos=False, case=False)
lost_df.sort_values(by='count', ascending=False)[:100]

https://babel.hathitrust.org/cgi/pt?id=bc.ark:/13960/t5q84bb6g&view=1up&seq=9

dubliners_volume = Volume("bc.ark:/13960/t5q84bb6g")

dubliners_volume.title

dubliners_volume.tokenlist().groupby(level='section').size()

from htrc_features import Volume
vol = Volume('data/ef2-stubby/hvd/34926/hvd.32044093320364.json.bz2')
vol

Volume("mdp.39015062571693").tokenlist().groupby(level='section').size()

