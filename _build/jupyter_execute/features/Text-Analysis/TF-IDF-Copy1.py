# TF-IDF

In this lesson, we're going to learn about a text analysis method called *term frequency–inverse document frequency* (tf–idf). This method will help us identify the most unique words in a document from a given corpus. 

### Simple Formula

Calculating the most frequent words in a text can be useful. But often the most *frequent words* in a text aren't the most *interesting* words in a text.

Term frequency-inverse document frequency is a method that tries to help with this problem becuase it identifies the most frequent *unique* words in a text by comparing it to other texts.

```{margin}
term = word <br>
document = text (or chunk of a text) <br>
corpus = collection of texts <br>
```

**term_frequency * inverse_document_frequency**

**term_frequency** = number of times a given term appears in document

**inverse_document_frequency** = log(total number of documents / number of documents with term) + 1

We're going to calculate and compare the tf–idf scores for the word *said* and the word *pigeons* in "The Girl Who Raised Pigeons," the first short story in *Lost in the City*.

We need the log() function for our calculation, so we're going to import it from the `math` package.

from math import log

**"said"**

total_number_of_documents = 14 ##total number of short stories in *Lost in the City*
number_of_documents_with_term = 13 ##number of short stories the contain the word "said"

term_frequency = 47 ##number of times "said" appears in "The Girl Who Raised Pigeons"
inverse_document_frequency = log(total_number_of_documents +1 / number_of_documents_with_term) + 1

term_frequency * inverse_document_frequency

**"pigeons"**

total_number_of_documents = 14 ##total number of short stories in *Lost in the City*
number_of_documents_with_term = 2 ##number of short stories the contain the word "pigeons"

term_frequency = 30 ##number of times "pigeons" appears in "The Girl Who Raised Pigeons"
inverse_document_frequency = log( (1+ total_number_of_documents) / (1+ number_of_documents_with_term)) + 1

tfidf = term_frequency * inverse_document_frequency

**tf–idf Scores**

"said" = 50.48<br>
"pigeons" = 88.38

Though the word "said" appears 47 times in "The Girl Who Raised Pigeons" and the word "pigeons" only appears 30 times, "pigeons" has a higher tf–idf score than "said" because it's a rarer word. The word "pigeons" appears in 2 of 14 stories, while "said" appears in 13 of 14 stories, almost all of them.

## tf–idf with scikit-learn

We could continue calculating tf–idf scores in this manner — by doing all the math with Python — but conveniently there's a Python library that can calculate tf–idf scores in just a few lines of code.

This library is called [scikit-learn](https://scikit-learn.org/stable/index.html), imported as `sklearn`. It's a popular Python library for machine learning approaches such as clustering, classification, and regression, among others. Though we're not doing any machine learning in this lesson, we're nevertheless going to use scikit-learn's `TfidfVectorizer` and `CountVectorizer`.

!pip install sklearn

#### Import Libraries

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
pd.set_option("max_rows", 600)
pd.set_option("max_columns", 200)
#pd.options.display.float_format = lambda value : '{:.0f}'.format(value) if round(value,0) == value else '{:,.3f}'.format(value)
from pathlib import Path  
import glob

We're also going to import `pandas` and change two of its default display settings. We're going to increase the maximum number of rows that pandas will display, and we're going to format numbers in a special way. If it's a decimal number, format to three decimal places; if it's a whole number, round to the whole number.

Finally, we're going to import two libraries that will help us work with files and the file system: [`pathlib`](https://docs.python.org/3/library/pathlib.html##basic-use) and [`glob`](https://docs.python.org/3/library/glob.html). These libraries will help us read in all the short story text files from *Lost in the City*.

#### Set Directory Path

Below we're setting the directory filepath that contains all the short story text files that we want to analyze.

directory_path = "../texts/literature/Lost-in-the-City_Stories/"

Then we're going to use `glob` and `Path` to make a list of all the short story filepaths in that directory and a list of all the short story titles.

text_files = glob.glob(f"{directory_path}/*.txt")

text_files

text_titles = [Path(text).stem for text in text_files]

text_titles

## Calculate tf–idf

To calculate tf–idf scores for every word, we're going to use scikit-learn's [`TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html).

When you initialize TfidfVectorizer, you can choose to set it with different parameters. These parameters will change the way you calculate tf–idf.

The recommended way to run `TfidfVectorizer`, however, is with smoothing (`smooth_idf = True`) and normalization (`norm='l2'`) turned on. These parameters will better account for differences in story length, and, overall, they'll produce more meaningful tf–idf scores. 

Smoothing and L2 normalization are actually the default settings for `TfidfVectorizer`. To turn them on, you don't need to include any extra code at all.

**Initialize TfidfVectorizer with desired parameters (default smoothing and normalization)**

tfidf_vectorizer = TfidfVectorizer(input='filename', stop_words='english')

**Plug in "text_files" which contains all our short stories**


directory_path = "../texts/literature/Lost-in-the-City_Stories/"

from sklearn.feature_extraction.text import CountVectorizer

#instantiate CountVectorizer()
cv=CountVectorizer(input='filename',stop_words='english') # using stopwords this time
 
# this steps returns word counts for the words in your docs 
word_count_vector=cv.fit_transform(text_files)

# check shape
word_count_vector.shape

cv.get_feature_names

pd.DataFrame(data=word_count_vector, index=index)

cv.vocabulary_

word_count_vector.vo

tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)

print(word_count_vector)

text_files = glob.glob(f"{directory_path}/*.txt")

text_titles = [Path(text).stem for text in text_files]

tfidf_vector = tfidf_vectorizer.fit_transform(text_files)

**Make a DataFrame out of the tf–idf vector and sort by title**

tfidf_df = pd.DataFrame(tfidf_vector.toarray(), index=text_titles, columns=tfidf_vectorizer.get_feature_names())
tfidf_df = tfidf_df.sort_index()

**Add column for number of times word appears in all documents**

tfidf_df.loc['Document Frequency'] = (tfidf_df > 0).sum()

tfidf_slice = tfidf_df[['pigeons', 'school', 'said', 'church', 'gospelteers', 'thunder','girl', 'street', 'father', 'dreaming', 'car']]
tfidf_slice

To find out the top 10 words with the highest tf–idf for every story, we're going to make and run the following function: `get_top_tfidf_scores()`

tfidf_slice.stack()

tfidf_df.stack().groupby(level=0).nlargest(10)

def get_top_tfidf_scores(series, top_n=10):
    pretty_df = series.stack().groupby(level=0).nlargest(top_n).reset_index()
    pretty_df = pretty_df.rename(columns={0:'tfidf_score', 'level_1': 'story', 'level_2': 'word'})
    pretty_df = pretty_df.drop(columns='level_0')
    pretty_df['tfidf_rank'] = pretty_df.groupby('story')['tfidf_score'].rank(method='first', ascending=False)
    return pretty_df

As before, this function will rearrange the dataframe, `.groupby()` short story, and filter for the top 10 highest tf–idf scores in every story. Finally, it will produce a dataframe with a new column `tfidf_rank`, which contains a 1-10 ranking of the highest tf–idf scores.

tfidf_df = tfidf_df.drop('Document Frequency', errors='ignore')

top_tfidf = get_top_tfidf_scores(tfidf_df)
top_tfidf

#### Write to a CSV File

filename = "tfidf_Lost-in-The-City.csv"
top_tfidf.to_csv(filename, encoding='UTF-8', index=False)



directory_path = "../texts/history/US_Inaugural_Addresses/"

text_files = glob.glob(f"{directory_path}/*.txt")

text_titles = [Path(text).stem for text in text_files]

tfidf_vector = tfidf_vectorizer.fit_transform(text_files)

**Make a DataFrame out of the tf–idf vector and sort by title**

tfidf_df = pd.DataFrame(tfidf_vector.toarray(), index=text_titles, columns=tfidf_vectorizer.get_feature_names())
tfidf_df = tfidf_df.sort_index()

**Add column for number of times word appears in all documents**

tfidf_df.loc['Document Frequency'] = (tfidf_df > 0).sum()

To find out the top 10 words with the highest tf–idf for every story, we're going to make and run the following function: `get_top_tfidf_scores()`

def get_top_tfidf_scores(series, top_n=10):
    pretty_df = series.stack().groupby(level=0).nlargest(top_n).reset_index()
    pretty_df = pretty_df.rename(columns={0:'tfidf_score', 'level_1': 'story', 'level_2': 'word'})
    pretty_df = pretty_df.drop(columns='level_0')
    pretty_df['tfidf_rank'] = pretty_df.groupby('story')['tfidf_score'].rank(method='first', ascending=False)
    return pretty_df

As before, this function will rearrange the dataframe, `.groupby()` short story, and filter for the top 10 highest tf–idf scores in every story. Finally, it will produce a dataframe with a new column `tfidf_rank`, which contains a 1-10 ranking of the highest tf–idf scores.

tfidf_df = tfidf_df.drop('Document Frequency', errors='ignore')

top_tfidf = get_top_tfidf_scores(tfidf_df)
top_tfidf

## Your Turn!

Take a few minutes to explore the dataframe below and then answer the following questions.

tfidf_compare

**1.** What is the difference between a tf-idf score and raw word frequency?

**Your answer here**

**2.** Based on the dataframe above, what is one potential problem or limitation that you notice with tf-idf scores?

**Your answer here**

**3.** What's another collection of texts that you think might be interesting to analyze with tf-idf scores?  Why?

**Your answer here**