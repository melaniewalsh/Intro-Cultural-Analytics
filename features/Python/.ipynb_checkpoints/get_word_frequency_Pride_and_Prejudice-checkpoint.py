#!/usr/bin/env python

#Import Libraries and Modules

from collections import Counter
import re
from spacy.lang.en.stop_words import STOP_WORDS

# Define Functions

def split_into_words(full_text):
    words = re.split(r"\W+", full_text.lower())
    return words 

# Define Filepaths

pride_prejudice_novel = "Pride-and-Prejudice-Novel.txt"

# Read files

with open(pride_prejudice_novel, encoding="utf-8") as file:
    full_text = file.read()
    
# Start Doing Stuff!

all_words = split_into_words(full_text)

words = [word for word in all_words if word not in STOP_WORDS]

words_frequency = Counter(words)

most_common_words = words_frequency.most_common(40)

print(most_common_words)
