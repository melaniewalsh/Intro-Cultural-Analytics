#!/usr/bin/env python


import argparse
import os
import glob

from collections import Counter
import re
from spacy.lang.en.stop_words import STOP_WORDS

## Define functions

def split_into_words(full_text):
    #words = re.split(r"\W+", full_text.lower())
    words = re.findall(r"[\w']+", full_text.lower())
    return words 

## Read in files and additional flags

parser = argparse.ArgumentParser()
parser.add_argument("--folder", help="input a folder or directory name")
parser.add_argument("--file", help="input a filename")
parser.add_argument("-n", "--number", type=int, help="define how many most frequent words you want returned", default=40)

user_input = parser.parse_args()

directory = user_input.folder
text_file = user_input.file
number_of_most_frequent_words = user_input.number
    
# Where the Action Happens

if text_file != None:

    with open(text_file, encoding="utf-8") as file:
        full_text = file.read()

    all_words = split_into_words(full_text)

    STOP_WORDS.add('s')

    words = [word for word in all_words if word not in STOP_WORDS]

    words_frequency = Counter(words)

    most_common_words = words_frequency.most_common(number_of_most_frequent_words)

    print(most_common_words)

elif directory != None:
    
    #print('folder')
    #print(os.path(directory))
    #print(glob.glob(f'{directory}/**/*.txt', recursive=True))
    all_files = glob.glob(f'{directory}/**/*.txt', recursive=True)
    words_frequency = Counter()
    
    for text_file in all_files:
         with open(text_file, encoding="utf-8") as file:
            full_text = file.read()

            all_words = split_into_words(full_text)

            STOP_WORDS.add('s')

            words = [word for word in all_words if word not in STOP_WORDS]

            words_frequency.update(words)

    most_common_words = words_frequency.most_common(number_of_most_frequent_words)

    print(most_common_words)

#     for filename in os.listdir(directory):
#         print(filename)
#         glob.glob('C:/Users/sam/Desktop/file1/**/*.txt', recursive=True)
#         if os.path.isfile(filename) \
#            and filename.endswith(".txt") \
#            and not filename in files:
#             with open(filename, "r") as file:
#                 all_files[filename] = file.read()
                
#                 all_words = split_into_words(all_files)

#                 STOP_WORDS.add('s')

#                 words = [word for word in all_words if word not in STOP_WORDS]

#                 words_frequency = Counter(words)

#                 most_common_words = words_frequency.most_common(number_of_most_frequent_words)

#                 print(most_common_words)
            