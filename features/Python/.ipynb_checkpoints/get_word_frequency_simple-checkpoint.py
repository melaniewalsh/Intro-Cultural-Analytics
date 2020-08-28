#!/usr/bin/env python


import sys

from collections import Counter
import re
from spacy.lang.en.stop_words import STOP_WORDS

# # Define functions

def split_into_words(full_text):
    words = re.findall(r"[\w']+", full_text.lower())
    return words 

# # Read in files

text_file = sys.argv[1]

# Where the Action Happens

with open(text_file, encoding="utf-8") as file:
    full_text = file.read()

all_words = split_into_words(full_text)

words = [word for word in all_words if word not in STOP_WORDS]

words_frequency = Counter(words)

most_common_words = words_frequency.most_common(40)

print(most_common_words)
