# Named Entity Recognition

In this lesson, we're going to learn about a text analysis method called *Named Entity Recognition* (NER). This method will help us computationally identify people, places, and things (of various kinds) in a text or collection of texts.

---

## Dataset

### Ada Lovelace's Obituary & Louisa May Alcott's *Little Women*

```{epigraph}
A century before the dawn of the computer age, Ada Lovelace imagined the modern-day, general-purpose computer. It could be programmed to follow instructions, she wrote in 1843. 

-- Claire Cain Miller, ["Ada Lovelace,"](https://www.nytimes.com/interactive/2018/obituaries/overlooked-ada-lovelace.html) *New York Times* Overlooked Obituaries
```

**Here's a preview of spaC's NER tagging Ada Lovelace's obituary:**

---

displacy.render(document, style="ent")

---

## Why is NER Useful?

Named Entity Recognition is useful for extracting key information from texts. You might use NER to identify the most frequently appearing characters in a novel or build a network of characters (something we'll do in a later lesson!). Or you might use NER to identify the geographic locations mentioned in texts, a first step toward mapping the locations (something we'll also do in a later lesson!).

## Natural Language Processing (NLP)

Named Entity Recognition is a fundamental task in the field of *natural language processing* (NLP). What is NLP, exactly? NLP is an interdisciplinary field that blends linguistics, statistics, and computer science. The heart of NLP is to understand human language with statistics and computers. Applications of NLP are all around us. Have you ever heard of a little thing called *spellcheck*? How about autocomplete, Google translate, chat bots, and Siri? These are all examples of NLP in action!

Thanks to recent advances in machine learning and to increasing amounts of available text data on the web, NLP has grown by leaps and bounds in the last decade. NLP models that generate texts are now getting eerily good. (If you don't believe me, check out [this app that will autocomplete your sentences](https://transformer.huggingface.co/doc/gpt2-large/qCNMTfzephfZMBkryTNvSRKQ/edit) with GPT-2, a state-of-the-art text generation model. When I ran it, the model generated a mini-lecture from a "university professor" that sounds spookily close to home...)

<img src="../images/GPT-2.png" id="image-border" >

Open-source NLP tools are getting very good, too. We're going to use one of these open-source tools, the Python library `spaCy`, for our Named Entity Recognition tasks in this lesson.

## How spaCy Works

The screenshot above shows spaCy correctly identifying named entities in Ada Lovelace's *New York Times* obituary (something that we'll test out for ourselves below). How does spaCy know that "Ada Lovelace" is a person and that "1843" is a date?

Well, spaCy doesn't *know*, not for sure anyway. Instead, spaCy is making a very educated guess. This "guess" is based on what spaCy has learned about the English language after seeing lots of other examples.

That's a colloquial way of saying: spaCy relies on machine learning models that were trained on a large amount of carefully-labeled texts. (These texts were, in fact, often labeled and corrected by hand). This is similar to our <a href="https://melaniewalsh.github.io/Intro-Cultural-Analytics/Text-Analysis/Topic-Modeling-Overview.html#1)-LDA-is-an-Unsupervised-Algorithm">topic modeling work</a> from the previous lesson, except our topic model wasn't using labeled data.

The English-language spaCy model that we're going to use in this lesson was trained on an annotated corpus called ["OntoNotes"](https://catalog.ldc.upenn.edu/docs/LDC2013T19/OntoNotes-Release-5.0.pdf): 2 million+ words drawn from "news, broadcast, talk shows, weblogs, usenet newsgroups, and conversational telephone speech," which were meticulously tagged by a group of researchers and professionals for people's names and places, for nouns and verbs, for subjects and objects, and much more. (Like a lot of other major machine learning projects, OntoNotes was also sponsored by the Defense Advaced Research Projects Agency (DARPA), the branch of the Defense Department that develops technology for the U.S. military.)

When spaCy identifies people and places in Ada Lovelace's obituary, in other words, the NLP model is actually making *predictions* about the text based on what it has learned about how people and places function in English-language sentences.

## NER with spaCy

### Install spaCy

!pip install -U spacy

### Import Libraries

We're going to import `spacy` and `displacy`, a special spaCy module for visualization.

import spacy
from spacy import displacy
from collections import Counter
import pandas as pd
pd.options.display.max_rows = 600
pd.options.display.max_colwidth = 400

We're also going to import the `Counter` module for counting people, places, and things, and the `pandas` library for organizing and displaying data (we're also changing the pandas default max row and column width display setting).

### Download Language Model

Next we need to download the English-language model (`en_core_web_sm`), which will be processing and making predictions about our texts. This is the model that was trained on the annotated "OntoNotes" corpus. You can download the `en_core_web_sm` model by running the cell below:

!python -m spacy download en_core_web_sm

*Note: spaCy offers [models for other languages](https://spacy.io/usage/models#languages) including German, French, Spanish, Portuguese, Italian, Dutch, Greek, Norwegian, and Lithuanian. Languages such as Russian, Ukrainian, Thai, Chinese, Japanese, Korean and Vietnamese don't currently have their own NLP models. However, spaCy offers language and tokenization support for many of these language with external dependencies — such as [PyviKonlpy](https://github.com/konlpy/konlpy) for Korean or [Jieba](https://github.com/fxsjy/jieba) for Chinese.*

### Load Language Model

Once the model is downloaded, we need to load it. There are two ways to load a spaCy language model.

**1.** We can import the model as a module and then load it from the module.

import en_core_web_sm
nlp = en_core_web_sm.load()

**2.** We can load the model by name.

#nlp = spacy.load('en_core_web_sm')

If you just downloaded the model for the first time, it's advisable to use Option 1. Then you can use the model immediately. Otherwise, you'll likely need to restart your Jupyter kernel (which you can do by clicking Kernel -> Restart Kernel.. in the Jupyter Lab menu).

## Process Document

We first need to process our `document` with the loaded NLP model. Most of the heavy NLP lifting is done in this line of code.

After processing, the `document` object will contain tons of juicy language data — named entities, sentence boundaries, parts of speech — and the rest of our work will be devoted to accessing this information.

In the cell below, we open and read Ada Lovelace's obituary. Then we run`nlp()` on the text and create our document.

filepath = "../texts/history/NYT-Obituaries/1852-Ada-Lovelace.txt"
text = open(filepath, encoding='utf-8').read()
document = nlp(text)

## spaCy Named Entities

Below is a Named Entities chart taken from [spaCy's website](https://spacy.io/api/annotation#named-entities), which shows the different named entities that spaCy can identify as well as their corresponding type labels.

|Type Label|Description|
|:---:|:---:|
|PERSON|People, including fictional.|
|NORP|Nationalities or religious or political groups.|
|FAC|Buildings, airports, highways, bridges, etc.|
|ORG|Companies, agencies, institutions, etc.|
|GPE|Countries, cities, states.|
|LOC|Non-GPE locations, mountain ranges, bodies of water.|
|PRODUCT|Objects, vehicles, foods, etc. (Not services.)|
|EVENT|Named hurricanes, battles, wars, sports events, etc.|
|WORK_OF_ART|Titles of books, songs, etc.|
|LAW|Named documents made into laws.|
|LANGUAGE|Any named language.|
|DATE|Absolute or relative dates or periods.|
|TIME|Times smaller than a day.|
|PERCENT|Percentage, including ”%“.|
|MONEY|Monetary values, including unit.|
|QUANTITY|Measurements, as of weight or distance.|
|ORDINAL|“first”, “second”, etc.|
|CARDINAL|Numerals that do not fall under another type.|


To quickly see spaCy's NER in action, we can use the [spaCy module `displacy`](https://spacy.io/usage/visualizers#ent) with the `style=` parameter set to "ent"  (short for entities):

displacy.render(document, style="ent")

From a quick glance at the text above, we can see that spaCy is doing quite well with NER. But it's definitely not perfect.

Though spaCy correctly identifies "Ada Lovelace" as a `PERSON` in the first sentence, just a few sentences later it labels her as a `WORK_OF_ART`. Though spaCy correctly identifies "London" as a place `GPE` a few paragraphs down, it incorrectly identifies "Jacquard" as a place `GPE`, too (when really "Jacquard" is a type of loom, named after [Marie Jacquard](https://en.wikipedia.org/wiki/Jacquard_machine)). 

This inconsistency is very important to note and keep in mind. If we wanted to use spaCy's NER for a project, it would almost certainly require manual correction and cleaning. And even then it wouldn't be perfect. That's why understanding the limitations of this tool is so crucial. While spaCy's NER can be very good for identifying entities in broad strokes, it can't be relied upon for anything exact and fine-grained — not out of the box anyway.

## Get Named Entities

All the named entities in our `document` can be found in the `document.ents` property. If we check out `document.ents`, we can see all the entities from Ada Lovelace's obituary.

document.ents

Each of the named entities in `document.ents` contains [more information about itself](https://spacy.io/usage/linguistic-features#accessing), which we can access by iterating through the `document.ents` with a simple `for` loop.

For each `named_entity` in `document.ents`, we will extract the `named_entity` and its corresponding `named_entity.label_`.

for named_entity in document.ents:
    print(named_entity, named_entity.label_)

To extract just the named entities that have been identified as `PERSON`, we can add a simple `if` statement into the mix:

for named_entity in document.ents:
    if named_entity.label_ == "PERSON":
        print(named_entity)

## NER with Long Texts or Many Texts

For the rest of this lesson, we're going to work with Edward P. Jones's short story collection *Lost in the City*, specifically the first story, "The Girl Who Raised Pigeons."

filepath = "../texts/literature/Little-Women.txt"
text = open(filepath).read()

import math
number_of_chunks = 80

chunk_size = math.ceil(len(text) / number_of_chunks)

text_chunks = []

for number in range(0, len(text), chunk_size):
    text_chunk = text[number:number+chunk_size]
    text_chunks.append(text_chunk)

chunked_documents = list(nlp.pipe(text_chunks))

## Get People

|Type Label|Description|
|:---:|:---:|
|PERSON|People, including fictional.|

To extract and count the people, we will use an `if` statement that will pull out words only if their "ent" label matches "PERSON."

people = []

for document in chunked_documents:
    for named_entity in document.ents:
        if named_entity.label_ == "PERSON":
            people.append(named_entity.text)

people_tally = Counter(people)

df = pd.DataFrame(people_tally.most_common(), columns=['character', 'count'])
df

## Get Places

|Type Label|Description|
|:---:|:---:|
|GPE|Countries, cities, states.|
|LOC|Non-GPE locations, mountain ranges, bodies of water.|

To extract and count places, we can follow the same model as above, except we will change our `if` statement to check for "ent" labels that match "GPE" or "LOC." These are the type labels for "counties cities, states" and "locations, mountain ranges, bodies of water."

places = []
for document in chunked_documents:
    for named_entity in document.ents:
        if named_entity.label_ == "GPE" or named_entity.label_ == "LOC":
            places.append(named_entity.text)

places_tally = Counter(places)

df = pd.DataFrame(places_tally.most_common(), columns=['place', 'count'])
df

## Get Streets & Parks

|Type Label|Description|
|:---:|:---:|
|FAC|Buildings, airports, highways, bridges, etc.|

To extract and count streets and parks (which show up a lot in *Lost in the City*!), we can follow the same model as above, except we will change our `if` statement to check for "ent" labels that match "FAC." This is the type label for "buildings, airports, highways, bridges, etc."

streets = []
for document in chunked_documents:
    for named_entity in document.ents:
        if named_entity.label_ == "FAC":
            streets.append(named_entity.text)

streets_tally = Counter(streets)

df = pd.DataFrame(streets_tally.most_common(), columns = ['street', 'count'])
df

## Get Works of Art

|Type Label|Description|
|:---:|:---:|
|WORK_OF_ART|Titles of books, songs, etc.|

To extract and count works of art, we can follow a similar-ish model to the examples above. This time, however, we're going to make our code even more economical and efficient (while still changing our `if` statement to match the "ent" label "WORK_OF_ART").

works_of_art = []
for document in chunked_documents:
    for named_entity in document.ents:
        if named_entity.label_ == "WORK_OF_ART":
            works_of_art.append(named_entity.text)

            art_tally = Counter(works_of_art)

df = pd.DataFrame(art_tally.most_common(), columns = ['work_of_art', 'count'])
df

## Get NER in Context

from IPython.display import Markdown, display
import re

def get_ner_in_context(keyword, document, desired_ner_labels= False):
    
    if desired_ner_labels != False:
        desired_ner_labels = desired_ner_labels
    else:
        desired_ner_labels = ['PERSON', 'NORP', 'FAC', 'ORG', 'GPE', 'LOC', 'PRODUCT', 'EVENT', 'WORK_OF_ART', 'LAW', 'LANGUAGE', 'DATE', 'TIME', 'PERCENT', 'MONEY', 'QUANTITY', 'ORDINAL', 'CARDINAL']  
        
    #Iterate through all the sentences in the document and pull out the text of each sentence
    for sentence in document.sents:
        #process each sentence
        sentence_doc = nlp(sentence.text)
        for named_entity in sentence_doc.ents:
            #Check to see if the keyword is in the sentence (and ignore capitalization by making both lowercase)
            if keyword.lower() in named_entity.text.lower()  and named_entity.label_ in desired_ner_labels:
                #Use the regex library to replace linebreaks and to make the keyword bolded, again ignoring capitalization
                #sentence_text = sentence.text
            
                sentence_text = re.sub('\n', ' ', sentence.text)
                sentence_text = re.sub(f"{named_entity.text}", f"**{named_entity.text}**", sentence_text, flags=re.IGNORECASE)

                display(Markdown('---'))
                display(Markdown(f"**{named_entity.label_}**"))
                display(Markdown(sentence_text))

for document in chunked_documents:
    get_ner_in_context('Jupiter', document)

## Your Turn!

Now it's your turn to take a crack at NER with a whole new text!


```{toggle}
|Type Label|Description|
|:---:|:---:|
|PERSON|People, including fictional.|
|NORP|Nationalities or religious or political groups.|
|FAC|Buildings, airports, highways, bridges, etc.|
|ORG|Companies, agencies, institutions, etc.|
|GPE|Countries, cities, states.|
|LOC|Non-GPE locations, mountain ranges, bodies of water.|
|PRODUCT|Objects, vehicles, foods, etc. (Not services.)|
|EVENT|Named hurricanes, battles, wars, sports events, etc.|
|WORK_OF_ART|Titles of books, songs, etc.|
|LAW|Named documents made into laws.|
|LANGUAGE|Any named language.|
|DATE|Absolute or relative dates or periods.|
|TIME|Times smaller than a day.|
|PERCENT|Percentage, including ”%“.|
|MONEY|Monetary values, including unit.|
|QUANTITY|Measurements, as of weight or distance.|
|ORDINAL|“first”, “second”, etc.|
|CARDINAL|Numerals that do not fall under another type.|
```

In this section, you're going to extract and count named entities from Barack Obama's memoir *The Audacity of Hope*. We're exploring Obama's memoir because it's chock full of named entities.

Open and read the text file

filepath = "../texts/literature/Obama-The-Audacity-of-Hope.txt"
text = open(filepath, encoding='utf-8').read()

To process *The Audacity of Hope* in smaller chunks (if working in Binder or on a computer with memory constraints):

chunked_text = text.split('\n')
chunked_documents = list(nlp.pipe(chunked_text))

To process *The Audacity of Hope* all at once (if working on a computer with a larger amount of memory):

document = nlp(text)

**1.** Choose a named entity from the possible spaCy named entities listed above. Extract, count, and make a dataframe from the most frequent named entities (of the type that you've chosen) in *The Audacity of Hope*. If you need help, study the examples above.

#Your Code Here 👇 

**2.** What is a result from this NER extraction that conformed to your expectations, that you find obvious or predictable? Why?

**#**Your answer here. (Double click this cell to type your answer.)

**3.** What is a result from this NER extraction that defied your expectations, that you find curious or counterintuitive? Why?

**#**Your answer here. (Double click this cell to type your answer.)

**4.** What's an insight that you might be able to glean about *The Audacity of Hope* based on your NER extraction?

**#**Your answer here. (Double click this cell to type your answer.)