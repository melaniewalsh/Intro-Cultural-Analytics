# Part-of-Speech Tagging 

In this lesson, we're going to learn about the textual analysis methods *part-of-speech tagging* and *keyword extraction*. These methods will help us computationally parse sentences and better understand words in context.

---

```{epigraph}
[Charles] Babbage, who called [Ada Lovelace] the “enchantress of numbers,” once wrote that she “has thrown her magical spell around the most abstract of Sciences and has grasped it with a force which few masculine intellects (in our own country at least) could have exerted over it.

-- Claire Cain Miller, ["Ada Lovelace,"](https://www.nytimes.com/interactive/2018/obituaries/overlooked-ada-lovelace.html) *NYT Overlooked Obituaries*
```

#Set some display options for the visualizer
options = {"compact": True, "distance": 50, "color": "yellow", "bg": "black", "font": "Gill Sans"}

displacy.render(document, style="dep", options=options)

---

## Why is Part-of-Speech Tagging Useful?

I don't mean to go all [Language Nerd](https://xkcd.com/1443/) on you, but parts of speech are important. Even if they seem kind of boring. *Parts of speech* are the grammatical units of language — such as (in English) nouns, verbs, adjectives, adverbs, pronouns, and prepositions. Each of these parts of speech plays a different role in a sentence.

<img src="https://imgs.xkcd.com/comics/language_nerd.png" >


By computationally identifying parts of speech, we can start computationally exploring *syntax*, the relationship between words — rather than only focusing on words in isolation, as we did with tf-idf. Though parts of speech may seem pedantic, they help computers (and us) crack at that ever-elusive abstract noun — *meaning*. 

## spaCy and Natural Language Processing (NLP)

To computationally identify parts of speech, we're going to use the natural language processing library spaCy. For a more extensive introduction to NLP and spaCy, see the previous lesson.

To parse sentences, spaCy relies on machine learning models that were trained on large amounts of labeled text data. The English-language spaCy model that we're going to use in this lesson was trained on an annotated corpus called ["OntoNotes"](https://catalog.ldc.upenn.edu/docs/LDC2013T19/OntoNotes-Release-5.0.pdf): 2 million+ words drawn from "news, broadcast, talk shows, weblogs, usenet newsgroups, and conversational telephone speech," which were meticulously tagged by a group of researchers and professionals for people's names and places, for nouns and verbs, for subjects and objects, and much more.

## Install spaCy

To use spaCy, we first need to install the library.

!pip install -U spacy

## Import Libraries

Then we're going to import `spacy` and `displacy`, a special spaCy module for visualization.

import spacy
from spacy import displacy
from collections import Counter
import pandas as pd
pd.set_option("max_rows", 400)
pd.set_option("max_colwidth", 400)

We're also going to import the `Counter` module for counting nouns, verbs, adjectives, etc., and the `pandas` library for organizing and displaying data (we're also changing the pandas default max row and column width display setting).

## Download Language Model

Next we need to download the English-language model (`en_core_web_sm`), which will be processing and making predictions about our texts. This is the model that was trained on the annotated "OntoNotes" corpus. You can download the `en_core_web_sm` model by running the cell below:

!python -m spacy download en_core_web_sm

*Note: spaCy offers [models for other languages](https://spacy.io/usage/models#languages) including German, French, Spanish, Portuguese, Italian, Dutch, Greek, Norwegian, and Lithuanian. Languages such as Russian, Ukrainian, Thai, Chinese, Japanese, Korean and Vietnamese don't currently have their own NLP models. However, spaCy offers language and tokenization support for many of these language with external dependencies — such as [PyviKonlpy](https://github.com/konlpy/konlpy) for Korean or [Jieba](https://github.com/fxsjy/jieba) for Chinese.*

## Load Language Model

Once the model is downloaded, we need to load it with `spacy.load()` and assign it to the variable `nlp`.

nlp = spacy.load('en_core_web_sm')

## Create a Processed spaCy Document

Whenever we use spaCy, our first step will be to create a processed spaCy `document` with the loaded NLP model `nlp()`. Most of the heavy NLP lifting is done in this line of code. After processing, the `document` object will contain tons of juicy language data — named entities, sentence boundaries, parts of speech — and the rest of our work will be devoted to accessing this information.

To test out spaCy's part-of-speech tagging, we'll begin by processing a sample sentence from Ada Lovelace's obituary:

> "[Charles] Babbage, who called [Ada Lovelace] the “enchantress of numbers,” once wrote that
she “has thrown her magical **spell** around the most **abstract** of Sciences and has grasped
it with a **force** which few masculine intellects (in our own country at least) could have exerted over it.

This sentence makes for an interesting example because it is syntactically complex and because it includes contains difficultly ambiguous words such as "spell," "abstract," and "force."

sample = """She “has thrown her magical spell around the most abstract of Sciences."""

document = nlp(sample)

## spaCy Part-of-Speech Tagging

| POS   | Description               | Examples                                      |
|:-----:|:-------------------------:|:---------------------------------------------:|
| ADJ   | adjective                 | big, old, green, incomprehensible, first      |
| ADP   | adposition                | in, to, during                                |
| ADV   | adverb                    | very, tomorrow, down, where, there            |
| AUX   | auxiliary                 | is, has (done), will (do), should (do)        |
| CONJ  | conjunction               | and, or, but                                  |
| CCONJ | coordinating conjunction  | and, or, but                                  |
| DET   | determiner                | a, an, the                                    |
| INTJ  | interjection              | psst, ouch, bravo, hello                      |
| NOUN  | noun                      | girl, cat, tree, air, beauty                  |
| NUM   | numeral                   | 1, 2017, one, seventy-seven, IV, MMXIV        |
| PART  | particle                  | ’s, not,                                      |
| PRON  | pronoun                   | I, you, he, she, myself, themselves, somebody |
| PROPN | proper noun               | Mary, John, London, NATO, HBO                 |
| PUNCT | punctuation               | ., (, ), ?                                    |
| SCONJ | subordinating conjunction | if, while, that                               |
| SYM   | symbol                    | $, %, §, ©, +, −, ×, ÷, =, :), 😝             |
| VERB  | verb                      | run, runs, running, eat, ate, eating          |
| X     | other                     | sfpksdpsxmsa                                  |
| SPACE | space                     |                                               |


Above is a POS chart taken from [spaCy's website](https://spacy.io/api/annotation#named-entities), which shows the different parts of speech that spaCy can identify as well as their corresponding labels. To quickly see spaCy's POS tagging in action, we can use the [spaCy module `displacy`](https://spacy.io/usage/visualizers#ent) on our sample `document` with the `style=` parameter set to "dep" (short for dependency parsing):

#Set some display options for the visualizer
options = {"compact": True, "distance": 90, "color": "yellow", "bg": "black", "font": "Gill Sans"}

displacy.render(document, style="dep", options=options)

As you can see, spaCy has correctly identified that "spell" and "force" are nouns in our sample sentence:

for token in document:
    if token.pos_ == "NOUN":
        print(token, token.pos_)

But if we look at the same words in a different context — in a sentence that I made up — spaCy can identify when these words have changed  grammatical roles and meanings.

> You shouldn't **force** someone to learn how to **spell** Babbage. They just need practice. You can't **abstract** it.

document = nlp("You shouldn't force someone to learn how to spell Babbage. They just need practice. You can't abstract it.")

for token in document:
    if token.pos_ == "VERB":
        print(token, token.pos_)

Where previously spaCy had identified "force" and "spell" as nouns, here spaCy correctly identifies the words "force," "spell," and "abstract" as verbs.

## Get Part-Of-Speech Tags

To get part of speech tags for every word in a document, we have to iterate through all the tokens in the document and pull out the `.pos_` attribute for each token. We can get even finer-grained dependency information with the attribute `.dep_`.


for token in document:
    print(token.text, token.pos_, token.dep_)

## Practicing with *Lost in the City*

For the rest of this lesson, we're going to explore Edward P. Jones's short story collection *Lost in the City*.

<img src="https://mybinder.org/static/images/logo_social.png" width="150" align="left" > *If you're using this Jupyter notebook in Binder (in the cloud), please uncomment the cell below and work with only the first story from _Lost in the City_. The Binder notebook is currently having issues loading the entire collection.*

#file = "../texts/literature/Lost-in-the-City_Stories/01-The-Girl-Who-Raised-Pigeons.txt"
#document = nlp(open(file).read())

filepath = "../texts/literature/Jones-Lost-in-The-City.txt"
document = nlp(open(filepath, encoding="utf-8").read())

## Get Adjectives

| POS   | Description               | Examples                                      |
|:-----:|:-------------------------:|:---------------------------------------------:|
| ADJ   | adjective                 | big, old, green, incomprehensible, first      |

To extract and count the adjectives in *Lost in the City*, we will follow the same model as above, except we'll add an `if` statement that will pull out words only if their POS label matches "ADJ."

```{admonition} Python Review!
:class: pythonreview
While we demonstrate how to extract parts of speech in the sections below, we're also going to reinforce some integral Python skills. Notice how we use `for` loops and `if` statements to `.append()` specific words to a list. Then we count the words in the list and make a pandas dataframe from the list.
```

Here we make a list of the adjectives identified in *Lost in the City*:

adjs = []
for token in document:
    if token.pos_ == 'ADJ':
        adjs.append(token.text)

adjs

Then we count the unique adjectives in this list with the `Counter()` module:

adjs_tally = Counter(adjs)

adjs_tally.most_common()

Then we make a dataframe from this list:

df = pd.DataFrame(adjs_tally.most_common(), columns=['character', 'count'])
df[:100]

## Get Nouns

| POS   | Description               | Examples                                      |
|:-----:|:-------------------------:|:---------------------------------------------:|
| NOUN  | noun                      | girl, cat, tree, air, beauty                  |

To extract and count nouns, we can follow the same model as above, except we will change our `if` statement to check for POS labels that match "NOUN".

nouns = []
for token in document:
    if token.pos_ == 'NOUN':
        nouns.append(token.text)

nouns_tally = Counter(nouns)

df = pd.DataFrame(nouns_tally.most_common(), columns=['noun', 'count'])
df[:100]

## Get Verbs

| POS   | Description               | Examples                                      |
|:-----:|:-------------------------:|:---------------------------------------------:|
| VERB  | verb                      | run, runs, running, eat, ate, eating          |

To extract and count works of art, we can follow a similar-ish model to the examples above. This time, however, we're going to make our code even more economical and efficient (while still changing our `if` statement to match the POS label "VERB").

```{admonition} Python Review!
:class: pythonreview
We can use a [*list comprehension*](https://melaniewalsh.github.io/Intro-Cultural-Analytics/Python/More-Lists-Loops.html#List-Comprehensions) to get our list of verbs in a single line of code! Closely examine the first line of code below:
```

verbs = [token.text for token in document if token.pos_ == 'VERB']

verbs_tally = Counter(verbs)

df = pd.DataFrame(verbs_tally.most_common(), columns=['verb', 'count'])
df[:100]

# Keyword Extraction

## Get Sentences with Keyword

spaCy can also identify sentences in a document. To access sentences, we can iterate through `document.sents` and pull out the `.text` of each sentence.

We can use spaCy's sentence-parsing capabilities to extract sentences that contain particular keywords, such as in the function below.

With the function `find_sentences_with_keyword()`, we will iterate through `document.sents` and pull out any sentence that contains a particular "keyword." Then we will display these sentence with the keywords bolded.

import regex
from IPython.display import Markdown, display

def find_sentences_with_keyword(keyword, document):
    
    #Iterate through all the sentences in the document and pull out the text of each sentence
    for sentence in document.sents:
        sentence = sentence.text
        
        #Check to see if the keyword is in the sentence (and ignore capitalization by making both lowercase)
        if keyword.lower() in sentence.lower():
            
            #Use the regex library to replace linebreaks and to make the keyword bolded, again ignoring capitalization
            sentence = re.sub('\n', ' ', sentence)
            sentence = re.sub(f"{keyword}", f"**{keyword}**", sentence, flags=re.IGNORECASE)
            
            display(Markdown(sentence))

find_sentences_with_keyword(keyword="mother", document=document)

## Get Keyword in Context

We can also find out about a keyword's more immediate context — its neighboring words to the left and right — and we can fine-tune our search with POS tagging.

To do so, we will first create a list of what's called *ngrams*. "Ngrams" are any sequence of *n* tokens in a text. They're an important concept in computational linguistics and NLP. (Have you ever played with [Google's *Ngram* Viewer](https://books.google.com/ngrams)?)

Below we're going to make a list of *bigrams*, that is, all the two-word combinations from *Lost in the City*. We're going to use these bigrams to find the neighboring words that appear alongside particular keywords.

#Make a list of tokens and POS labels from document if the token is a word 
tokens_and_labels = [(token.text, token.pos_) for token in document if token.is_alpha]

#Make a function to get all two-word combinations
def get_bigrams(word_list, number_consecutive_words=2):
    
    ngrams = []
    adj_length_of_word_list = len(word_list) - (number_consecutive_words - 1)
    
    #Loop through numbers from 0 to the (slightly adjusted) length of your word list
    for word_index in range(adj_length_of_word_list):
        
        #Index the list at each number, grabbing the word at that number index as well as N number of words after it
        ngram = word_list[word_index : word_index + number_consecutive_words]
        
        #Append this word combo to the master list "ngrams"
        ngrams.append(ngram)
        
    return ngrams

bigrams = get_bigrams(tokens_and_labels)

Let's take a peek at the bigrams:

bigrams[5:20]

Now that we have our list of bigrams, we're going to make a function `get_neighbor_words()`. This function will return the most frequent words that appear next to a particular keyword. The function can also be fine-tuned to return neighbor words that match a certain part of speech by changing the `pos_label` parameter.

def get_neighbor_words(keyword, bigrams, pos_label = None):
    
    neighbor_words = []
    keyword = keyword.lower()
    
    for bigram in bigrams:
        
        #Extract just the lowercased words (not the labels) for each bigram
        words = [word.lower() for word, label in bigram]        
        
        #Check to see if keyword is in the bigram
        if keyword in words:
            
            for word, label in bigram:
                
                #Now focus on the neighbor word, not the keyword
                if word.lower() != keyword:
                    #If the neighbor word matches the right pos_label, append it to the master list
                    if label == pos_label or pos_label == None:
                        neighbor_words.append(word.lower())
    
    return Counter(neighbor_words).most_common()

get_neighbor_words("mother", bigrams)

get_neighbor_words("mother", bigrams, pos_label='ADJ')

## Your Turn!

Try out `find_sentences_with_keyword()` and `get_neighbor_words` with your own keywords of interest.

find_sentences_with_keyword(keyword="YOUR KEY WORD", document=document)

get_neighbor_words(keyword="YOUR KEY WORD", bigrams, pos_label=None)