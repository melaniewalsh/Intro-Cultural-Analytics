## More Lists & Loops, Plus Modules

[Download relevant files here](https://melaniewalsh.org/More-Lists-Loops.zip)

Last lesson, we learned how to make, manipulate, and iterate through lists, an important Python collection type. But we weren't actually working with a real CSV file, and we weren't doing a very comprehensive analysis of the data. In this lesson, we're going to work with a real CSV file and try to answer some analytical questions about the Bellevue Almshouse data, such as:

- What is the most common "disease" and the least common "disease"?
- What is the most common "profession" and the least common "profession"?
- What is the gender breakdown of those admitted to the Bellevue Almshouse?

We're going to answer these questions by practicing more with lists and loops while also introducing the csv module and the collections module.

import pandas
pandas.read_csv("../data/bellevue_almshouse_modified.csv").head(20)

## Reading in a CSV File

The [csv module](https://docs.python.org/3/library/csv.html) allows you to read and write tabular data in CSV (comma separated values) format, one of the most common formats for spreadsheets. (Soon we're going to talk about the [Python library Pandas](https://melaniewalsh.github.io/Intro-Cultural-Analytics/Python/Pandas.html), an even more powerful and more convenient way of working with tabular data.)

import csv

To use the csv module, you have to first import it, as above. Then to read in a CSV file, as below, you need to `with open()` your desired CSV file `as` a csv object `:` then use the `csv.reader()` function and insert your csv object. The "delimiter" argument tells the computer how to read the CSV file. Sometimes you might have a CSV file that is separated by tabs (\t) instead of commas (,) so it's typically good to specify.

almshouse_filepath = '../data/bellevue_almshouse_modified.csv'

with open(almshouse_filepath) as csv_object:
    almshouse_data = csv.reader(csv_object, delimiter=',')

almshouse_data

The `csv.reader()` function will create a "reader object." To actually get at the data in there, we'll need to iterate through it in some way. Each row in the reader object is a list of strings, so if we iterate through every row in the dataset, we will get 9,000+ lists (!). It's helpful to remember what each row in the dataset represents and name your variables accordingly. For the Bellevue Almshouse dataset, each row represents a person.

with open(almshouse_filepath) as csv_object:
    almshouse_data = csv.reader(csv_object, delimiter=',')
    
    for person in almshouse_data:
        print(person)

**Pro tip!** If you have a really long output, you can ["Enable Scrolling for Outputs"](https://melaniewalsh.github.io/Intro-Cultural-Analytics/images/enable-scrolling.png) by right-clicking and selecting that option.

If we wanted to answer our first question — *What is the most common "disease" and the least common "disease"?* — how might we isolate only the names of the diseases so we can count them? Think back to how [we indexed a list](https://melaniewalsh.github.io/Intro-Cultural-Analytics/Python/Lists-Loops.html#Index) in the last lesson...

with open(almshouse_filepath) as csv_object:
    almshouse_data = csv.reader(csv_object, delimiter=',')
    
    for person in almshouse_data:
        print(person[0])

with open(almshouse_filepath) as csv_object:
    almshouse_data = csv.reader(csv_object, delimiter=',')
    
    for person in almshouse_data:
        print(person[4])

### Build a List With a `For` Loop

Great! We figured out how to isolate the diseases. But to count them, we want to get them in a data collection of their own, like a list. How would we put this data into a list? Let's make an empty list and then append each disease from each row into the list.

❌ ❌ ❌ **Not Correct**

with open(almshouse_filepath) as csv_object:
    almshouse_data = csv.reader(csv_object, delimiter=',')
    
    for person in almshouse_data:
        diseases = []
        diseases.append(person[4])

diseases

Wait, that's not quite right. We only got a list with a single value. What's going on?

The problem is that the list building is happening *inside* the `for` loop. This means that, `for` every person/row, the list is being re-written over and over again. "destitution" is the very last disease in the dataset, so we're only getting the very last value. To keep building on a list, we need to put the empty list *outside* of the `for` loop and then keep adding to it.

with open(almshouse_filepath) as csv_object:
    almshouse_data = csv.reader(csv_object, delimiter=',')
    
    diseases = []
    for person in almshouse_data:   
        diseases.append(person[4])

diseases

## Measure Length of List

To measure the length of a list, use the `len()` function.

len(diseases)

## Count Items In a List or Collection

The Counter tool from the collections module is extremely useful. It can help you count all kinds of things. To use it, you first need to `import` the Counter `from` collections.

from collections import Counter

To count something, you simply need to insert it inside the `Counter()` function, like so:

Counter(diseases)

This will give you what's called a dictionary, which includes every disease in the dataset and how many times it appears. To sort this Counter dictionary based on the most common items, you can use the `.most_common()` method.

disease_tally = Counter(diseases)
disease_tally.most_common()

You can also select a certain number of the most common items by placing a number inside the `.most_common()` method.

disease_tally.most_common(10)

You can also select a certain number of the *least* common items by extracting a slice from the end of list, like so:

disease_tally.most_common()[-10:]

disease_tally.most_common()[-3:]

## Your Turn!

By using the same methods, find the 10 most common professions and the 10 least common professions in the Bellevue Almshouse dataset.

Build a list called `professions` by using a `for` loop and the `.append()` method.

with open(almshouse_filepath) as csv_object:
    almshouse_data = csv.reader(csv_object, delimiter=',')
    
    #Your Code Here
    for person in almshouse_data:   
        #Your Code Here

professions

Count the list `professions` with the Counter tool then display the top 10 most common values.

from collections import Counter

professions_tally = #Your Code Here
#Your Code Here

Display the 10 least common values.

#Your Code Here

Now find out how many men vs women are included in the Bellevue Almshouse data. Build a list called `gender` with a `for` loop and the `.append()` method

with open(almshouse_filepath) as csv_object:
    almshouse_data = csv.reader(csv_object, delimiter=',')
    
    #Your Code Here
    for person in almshouse_data:   
        #Your Code Here

gender

Count the values in the gender column wiht the Counter tool and then display the results.

from collections import Counter

gender_tally = #Your Code Here
gender_tally

## List Comprehensions

There's a slightly easier and more compact way to build a list with a `for` loop called a "list comprehension." Instead of creating an empty list, you can build the `for` loop inside of a list.

<img src='../images/lists/list-comprehensions' width=100% >

with open(almshouse_filepath) as csv_object:
    almshouse_data = csv.reader(csv_object, delimiter=',')
    
    diseases = [person[4] for person in almshouse_data]

diseases

Remember our Python script for counting words in a text file? Though you probably didn't recognize it at the time, this code contains a list comprehension. Can you spot it?

import re
from collections import Counter
from nltk.corpus import stopwords

def split_into_words(any_chunk_of_text):
    lowercase_text = any_chunk_of_text.lower()
    split_words = re.split("\W+", lowercase_text)
    return split_words

filepath_of_text = "../texts/literature/The-Yellow-Wallpaper.txt"
nltk_stop_words = stopwords.words("english")
number_of_desired_words = 40

full_text = open(filepath_of_text, encoding="utf-8").read()

all_the_words = split_into_words(full_text)
meaningful_words = [word for word in all_the_words if word not in nltk_stop_words]
meaningful_words_tally = Counter(meaningful_words)
most_frequent_meaningful_words = meaningful_words_tally.most_common(number_of_desired_words)

print(most_frequent_meaningful_words)

This is the list comprehension:

meaningful_words = [word for word in all_the_words if word not in nltk_stop_words]

which is exactly the same as

meaningful_words = []
for word in all_the_words:
    if word not in nltk_stop_words:
        meaningful_words.append(word)



empty_string = []
    for item in collection:
        if item in items_we_want:
            empty_string.append(item)

empty_string = [item for item in collection if item in items_we_want]