# Song Lyrics Analysis

Since we now have access to all these great song lyrics, let's run some basic analyses on them. 

## Loop Through All Text Files in Directory

from pathlib import Path

directory_path = 'Missy-Elliott_Under-Construction/'

for file in Path(directory_path).glob('*.txt'):
    print(file)

## Count Words in Each File in Directory

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
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
             'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 've', 'll', 'amp']

from collections import Counter
import re

def split_into_words(any_chunk_of_text):
    lowercase_text = any_chunk_of_text.lower()
    split_words = re.split("\W+", lowercase_text)
    return split_words 

def get_most_frequent_words_directory(directory_path):
    
    number_of_desired_words = 20
    meaningful_words_tally = Counter()
    
    for filepath in Path(directory_path).glob('*.txt'):
            
            full_text = open(filepath, encoding="utf-8").read()
            all_the_words = split_into_words(full_text)
            meaningful_words = [word for word in all_the_words if word not in stopwords]
            meaningful_words_tally.update(meaningful_words)
    
    most_frequent_meaningful_words = meaningful_words_tally.most_common(number_of_desired_words)

    return most_frequent_meaningful_words

get_most_frequent_words_directory("Missy-Elliott_Under-Construction")

## Word Count Data Viz with Pandas

import pandas as pd

frequencies = get_most_frequent_words_directory("Missy-Elliott_Under-Construction")

#Make Counter dictionary into a Pandas DataFrame
word_frequency_df = pd.DataFrame(frequencies, columns=['word', 'word_count'])
#Plot word counts
word_frequency_df.sort_values(by='word_count').plot(x='word', kind='barh', title="Missy Elliott's Under Construction:\n Most Frequent Words")

## Keywords in Context

from IPython.display import Markdown, display
from pathlib import Path

keyword = "ti"

for filepath in Path(directory_path).glob('*.txt'):
    text = open(filepath).read()
    
    for line in text.split("\n"):
        #Search for keyword
        if re.search(f"\\b{keyword}\\b", line):
            #Replace keyword with bolded keyword
            line_with_bolding = re.sub(f"\\b{keyword}\\b", f"**{keyword}**", line, flags=re.IGNORECASE)
            #Display line with bolded keyword
            display(Markdown(line_with_bolding))

keyword = "Missy"

for filepath in Path(directory_path).glob('*.txt'):
    text = open(filepath).read()
    
    for line in text.split("\n"):
        #Search for keyword
        if re.search(f"\\b{keyword}\\b", line):
            #Replace keyword with bolded keyword
            line_with_bolding = re.sub(f"\\b{keyword}\\b", f"**{keyword}**", line, flags=re.IGNORECASE)
            #Display line with bolded keyword
            display(Markdown(line_with_bolding))