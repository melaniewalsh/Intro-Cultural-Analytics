# Dictionaries

In this lesson, we're going to learn about Python dictionaries by drawing on Anelise Shrout's [Bellevue Almshouse Dataset](https://www.nyuirish.net/almshouse/the-almshouse-records/), excerpted below.

**Preview The Bellevue Almshouse Dataset**

import pandas
pandas.read_csv("../data/bellevue_almshouse_modified.csv").head(20)

```{margin} The Bellevue Almshouse Dataset 
The Bellevue Almshouse Dataset includes information about Irish-born immigrants who were admitted to the almshouse in the 1840s. The Bellevue Almshouse was part of New York City's public health system, a place where poor, sick, homeless, and otherwise marginalized people were sent — sometimes voluntarily and sometimes forcibly. This dataset was transcribed from the almshouse's own admissions records by Anelise Shrout.
```

We're using the [Bellevue Almshouse Dataset](https://www.nyuirish.net/almshouse/the-almshouse-records/) to practice dictionaries because we want to think deeply about the consequences of reducing human life to data even at this early stage in our Python journey. This immigration data, as Shrout argues in her essay ["(Re)Humanizing Data: Digitally Navigating the Bellevue Almshouse,"](https://crdh.rrchnm.org/essays/v01-10-(re)-humanizing-data/) was "produced with the express purpose of reducing people to bodies; bodies to easily quantifiable aspects; and assigning value to those aspects which proved that the marginalized people to who they belonged were worth less than their elite counterparts."

___

## Dictionary

When we used lists with the Bellevue Almshouse data, it was easier than individually assigning individual variables. We could put multiple names into a single list and multiple ages in a single list.

By using a Python data collection type called a *dictionary*, we can go even further and group each person's name, age, and profession into a single collection.

**Indivudal Variables**

person1_name = 'Mary Gallagher'
person2_name = 'John Sanin (?)'
person1_age = 18
person2_age = 19

**Lists**

names = ['Mary Gallagher', 'John Sanin(?)', 'Anthony Clark', 'Margaret Farrell']
ages = [28, 19, 60, 30]
professions = ['married', 'laborer', 'laborer', 'widow']

**Dictionary**

person1 = {"name": "Mary Gallagher",
             "age": 28,
             "profession": "married"}

type(person1)

person2 = {"name": "John Sanin(?)",
             "age": 19,
             "profession": "laborer"}

## Key-Value

A dictionary is made up of "key"-"value" pairs, which are separated by a colon `:` and separated from other key-value pairs by a comma `,`. A dictionary is always enclosed by curly brackets `{}`. 

person1 = {"name": "Mary Gallagher",
             "age": 28,
             "profession": "married"}

You can check all the keys in a dictionary by using the `.keys()` method or all the values in a dictionary by using the `.values()` method.

person1.keys()

person1.values()

## Access Items

You can access a value in a dictionary by using square brackets `[]` and its key name (kind of like how we indexed a string or a list).

person1["name"]

person1["age"]

person1["profession"]

## Change Item

You can change a value in a dictionary by re-assigning a new value to a dictionary key.

person1["age"] = 100

person1

person1['profession'] = 'spinster'

person1

## Nested Dictionary

You can also nest a dictionary inside another dictionary.

bellevue_people = {
                "person1":
                  {"name": "Mary Gallagher",
                   "age": 28,
                   "profession": "married"},
                "person2":
                  {"name": "John Sanin(?)",
                   "age": 19,
                   "profession": "laborer"}
                }

bellevue_people['person1']

bellevue_people['person1']['name']

bellevue_people['person2']

bellevue_people['person2']['age']

## Iterate Through Dictionary

for person in bellevue_people.keys():
    print(person)

for person in bellevue_people.values():
    print(person)

for person in bellevue_people.values():
    if person['age'] > 20:
        name = person['name']
        age = person['age']
        print(f'{name} is more than 20 years old. She is {age}.')

for person in bellevue_people.items():
    print(person)