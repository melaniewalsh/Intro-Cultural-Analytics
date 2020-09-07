# Make a Character Network

This lesson demonstrates how to create a social network of people mentioned in a text based on how often people appear within a certain distance of one another.

#!pip install spacy
#!python -m spacy download en_core_web_sm

## Import Libraries

import spacy
import en_core_web_sm
from collections import Counter
import pandas as pd
pd.set_option("max_rows", 400)
import networkx 
import itertools

## Load spaCy Language Model

#nlp = spacy.load('en_core_web_sm')
nlp = en_core_web_sm.load()

## Character Networks For Shorter Texts

This section demonstrates how to create a character network from a text if you can process the entire text with spaCy at one time (mostly shorter texts).

### Read in Text File

filepath = "../texts/literature/Jones-Lost-in-The-City.txt"
text = open(filepath).read()

### Process Text

document = nlp(text)

### Create or Upload List of Characters

If you already have a list of characters that you'd like to identify, skip to the end of this section. If you'd like to identify characters with spaCy's NER tagger, run the code below:

spacy_identified_people = []

for named_entity in document.ents:
    if named_entity.label_ == "PERSON":
        
        spacy_identified_people.append(named_entity.text)

Then output this list of spaCy's identified people to a CSV file for manual cleaning and editing:

pd.DataFrame(Counter(spacy_identified_people).most_common(), columns=['character', 'count']).to_csv('spacy-identified-people.csv', index=False)

Read in a CSV file with a cleaned list of characters in a column titled "character":

my_list_of_characters = pd.read_csv('My-Cleaned-Character-List.csv')['character'].tolist()

Uncomment to re-upload the CSV file without cleaning or editing:

#my_list_of_characters = pd.read_csv('spacy-identified-people.csv')['character'].tolist()

### Find Character, Index in Document

Count any named entity that matches a person in the list of characters. Also extract the index number where that person appears in the document, so we can later calculate characters who appear near one another.

all_people_matches = []
all_people_matches_plus_ids = []

#Get all entity matches for a previously identified person
for named_entity in document.ents:
    if named_entity.text in my_list_of_characters:
        person = named_entity.text
        
        #Remove apostrophe 's from character name
        person = person.replace("’s", "").strip()
        #Get the character index number from the text
        person_index = named_entity.start_char
        
        all_people_matches.append(person)
        all_people_matches_plus_ids.append([person, person_index])

### Make List of Edges

Compare every character to every other character in the list. If two characters fall within 50 characters of one another, add them to the `edge_list`. To change the number of characters, simply change the `threshold_distance` variable below:

edge_list = []

threshold_distance = 50

#If two people fall within 50 characters of one another, add them to the edge list
for person, another_person in itertools.combinations(all_people_matches_plus_ids, 2):
        distance = abs(person[1] - another_person[1])
        
        if distance < threshold_distance:
            
            if person[0] != another_person[0]:
                
                edge_list.append((person[0], another_person[0]))

### Make Network DataFrame

character_df = pd.DataFrame(Counter(edge_list).most_common(), columns=['character_pair', 'Weight'])
character_df['Source']=character_df['character_pair'].str[0]
character_df['Target']=character_df['character_pair'].str[1]

character_network = character_df[['Source', 'Target', 'Weight']]
character_network

### Output Network as Graphml File

G = networkx.from_pandas_edgelist(character_network, "Source", "Target", "Weight")
networkx.write_graphml(G, "Lost-in-the-City-network.graphml")

### Output Network as CSV File

character_network.to_csv("Lost-in-the-City-network.csv")

## Character Networks For Longer Texts

This section demonstrates how to create a character network from a text if you cannot process the entire text with spaCy at one time and need to chunk it into smaller documents (mostly longer texts).

filepath = "../texts/literature/Little-Women.txt"
text = open(filepath).read()

### Chunk Text By Number of Chunks

To chunk text by a specific number of chunks, choose a `number_of_chunks` value and run the cell below. The current default value is 80 chunks. 

import math
number_of_chunks = 80
chunk_size = math.ceil(len(text) / number_of_chunks)
chunked_text = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

The code above is dividing the total number of characters in the text `len(text)` by the number of chunks you want, then rounding up `math.ceil()` to a whole number. This is calculating the necessary chunk size for the number of chunks you want. The final line iterates through the text and creates slices at the necessary chunk size.

### Or Chunk Text By Line Breaks

#chunked_text= text.split('\n')

### Process Chunked Text

chunked_documents = list(nlp.pipe(chunked_text))

### Create or Upload List of Characters

If you already have a list of characters that you'd like to identify, skip to the end of this section. If you'd like to identify characters with spaCy's NER tagger, run the code below:

spacy_identified_people = []

for document in chunked_documents:
    for named_entity in document.ents:
        if named_entity.label_ == "PERSON":
            spacy_identified_people.append(named_entity.text)

Output list of identified people to a CSV file for manual cleaning and editing:

pd.DataFrame(Counter(spacy_identified_people).most_common(), columns=['character', 'count']).to_csv('spacy-identified-people.csv', index=False)

Read in a CSV file with a cleaned list of characters in a column titled "character":

my_list_of_characters = pd.read_csv('My-Cleaned-Character-List.csv')['character'].tolist()

Uncomment to re-upload the CSV file without cleaning or editing:

#my_list_of_characters = pd.read_csv('spacy-identified-people.csv')['character'].tolist()

### Find Character, Index in Document(s)

Count any named entity that matches a person in the list of characters. Also extract the index number where that person appears in the document, so we can later calculate characters who appear near one another.

all_people_matches = []
all_people_matches_plus_ids = []
document_length = 0

for document in chunked_documents:
    document_length += len(document.text)
    for named_entity in document.ents:
        if named_entity.text in my_list_of_characters:
            person = named_entity.text

            #Remove apostrophe 's from character name
            person = person.replace("’s", "").strip()
            
            #Get the character index number from the text
            person_index =  (document_length - named_entity.start_char)

            all_people_matches.append(person)
            all_people_matches_plus_ids.append([person, person_index])

### Make List of Edges

Compare every character to every other character in the list. If two characters fall within 100 characters of one another, add them to the `edge_list`.

edge_list = []

threshold_distance = 100

#Get all entity matches for a previously identified person
for person, another_person in itertools.combinations(all_people_matches_plus_ids, 2):
        distance = abs(person[1] - another_person[1])
        if distance < threshold_distance:
            
            if person[0] != another_person[0]:
                
                edge_list.append((person[0], another_person[0]))

### Make Network DataFrame

character_df = pd.DataFrame(Counter(edge_list).most_common(), columns=['character_pair', 'Weight'])
character_df['Source']=character_df['character_pair'].str[0]
character_df['Target']=character_df['character_pair'].str[1]

character_network = character_df[['Source', 'Target', 'Weight']]
character_network

### Filter Network By Edge Weights

character_network[character_network['Weight'] > 2]

### Output Network as Graphml File

G = networkx.from_pandas_edgelist(character_network, "Source", "Target", "Weight")
networkx.write_graphml(G, "Little-Women-network.graphml")

### Output Network as CSV File

character_network.to_csv("Little-Women-network.csv")