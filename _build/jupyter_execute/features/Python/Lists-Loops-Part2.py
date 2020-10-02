# Lists & Loops — Part 2

In this lesson, we're going to learn more about lists and loops by drawing on DH scholar Anelise Shrout's [Bellevue Almshouse Dataset](https://www.nyuirish.net/almshouse/the-almshouse-records/).

**Preview The Bellevue Almshouse Dataset**

import pandas
pandas.read_csv("../data/bellevue_almshouse_modified.csv").head(20)

```{margin} The Bellevue Almshouse Dataset 
The Bellevue Almshouse Dataset includes information about Irish-born immigrants who were admitted to the almshouse in the 1840s. The Bellevue Almshouse was part of New York City's public health system, a place where poor, sick, homeless, and otherwise marginalized people were sent — sometimes voluntarily and sometimes forcibly. This dataset was transcribed from the almshouse's own admissions records by Anelise Shrout.
```

We're using the Bellevue Almshouse Dataset to practice Python lists and loops because we want to think deeply about the consequences of reducing human life to data even at this early stage in our Python journey. This immigration data, as Shrout argues in her essay ["(Re)Humanizing Data: Digitally Navigating the Bellevue Almshouse,"](https://crdh.rrchnm.org/essays/v01-10-(re)-humanizing-data/) was "produced with the express purpose of reducing people to bodies; bodies to easily quantifiable aspects; and assigning value to those aspects which proved that the marginalized people to who they belonged were worth less than their elite counterparts."

As we work through the lesson below, reflect about the categories that these Irish immigrants were slotted into by the NYC government. What should we make of the fact that Python, as a programming language, doesn't understand the meaning or historical context of this data? How can we nevertheless use Python to better understand this history and to interrogate power?

---

In the previous lesson, we learned how to make, manipulate, and iterate through lists, an important Python collection type. In this lesson, we're going to keep practicing and learn how to:

- build lists with `for` loops
- create a running index of items in a list with `enumerate()`
- create one-line `for` loops with *list comprehensions*
- zip lists together with`zip()`
- easily count items in a list

These tools can help us:

- identify how many times a certain value appears in the data (e.g., the so-called disease "recent emigrant")
- programatically change all blank values in the data (e.g., from a blank to "no disease recorded")
- find the most and least common values in the data (e.g., most common "diseases" or professions)

**Example Lists**

Here are the four lists with sample data from the Bellevue Almshouse dataset. Each item in each list corresponds to a single row from the dataset. You might imagine how the code in this lesson might apply to the entire dataset or to other large datasets.

first_names = ['Unity', 'Catherine', 'Thomas', 'William', 'Patrick', 'Mary Anne', 'Morris',
               'Michael', 'Ellen', 'James', 'Michael', 'Hannah', 'Alexander', 'Mary A', 'Serena?',
               'Margaret', 'Michael', 'Jane', 'Rosanna', 'James', 'Michael', 'John', 'John', 'Mary',
               'Bantel', 'Marcella', 'Arthur', 'Michael', 'Mary', 'Martin']

last_names =  ['Harkin', 'Doyle', 'McDonald', 'Jordan', 'Rouse', 'Keene', 'Brown',
               'McLoughlin', 'Cassidy', 'Whittle', 'Coyle', 'Cullen', 'Cozens', 
               'Maly', 'McGuire', 'Laly', 'Bahan', 'Combs', 'McGovern', 'Gallagher', 
               'Crone', 'Brannon', 'McDonal', 'Atkins', 'Garragan', 'Wood', 'Kelly', 'Galeny', 'Welch', 'Kerly']

diseases = ['', 'recent emigrant', 'sickness', '', '', '', 'destitution', '', 'sickness', '',
            'sickness', 'recent emigrant', '', 'insane', 'recent emigrant', 'insane', '', '',
            'sickness', 'sickness', '', 'syphilis', 'sickness', '', 'recent emigrant', 'destitution',
            'sickness', 'recent emigrant', 'sickness', 'sickness']

ages = ['22', '21', '23', '47', '45', '28', '23', '50', '26', '28', '30', '30', '65', '17', '35',
        '27', '32', '40', '22', '30', '27', '40', '41', '37', '16', '20', '30', '30', '35', '9']

## For Loop

As a refresher, we can use a `for` loop to iterate through a list and do something to each item in the list.


diseases = ['', 'recent emigrant', 'sickness', '', '', '', 'destitution', '', 'sickness', '',
            'sickness', 'recent emigrant', '', 'insane', 'recent emigrant', 'insane', '', '',
            'sickness', 'sickness', '', 'syphilis', 'sickness', '', 'recent emigrant', 'destitution',
            'sickness', 'recent emigrant', 'sickness', 'sickness']

Below we are iterating through the list `diseases` and printing out every item in the list.

for disease in diseases:
    print(disease)

Remember that the variable name that will represent each item in the list doesn't exist yet, and it can be named anything you want. Instead of `disease`, we could name the variable `x`

for x in diseases:
    print(x)

As we've discussed before, however, it's preferable to name your variables something clear that has human language significance.

## Enumerate()

diseases = ['', 'recent emigrant', 'sickness', '', '', '', 'destitution', '', 'sickness', '',
            'sickness', 'recent emigrant', '', 'insane', 'recent emigrant', 'insane', '', '',
            'sickness', 'sickness', '', 'syphilis', 'sickness', '', 'recent emigrant', 'destitution',
            'sickness', 'recent emigrant', 'sickness', 'sickness']

You might want to keep a numerical count or index of items in a list. To print out each item in the list with a corresponding number, you can use the built-in Python function `enumerate()`.

To access the number that corresponds to each item, you need to unpack *two* variables instead of just one: `number` , `disease`

for number, disease in enumerate(diseases):
    print(number, disease)

for number, disease in enumerate(diseases):
    print(f"Person {number}: {disease}")

## Build a List with a `For` Loop

We can also make lists with `for` loops. Let's say we wanted to take this list `collection` and create a new list that only contains the items in the list that match `"item we want"`.

collection = ['item', 'item we want', 'item', 'item', 'item we want']

To do so, we could make an empty list by assigning `empty_list` the value of `[]`—that is, a list with nothing inside of it.  
Then, we could use a `for` loop to iterate through `collection`. If an item equals `"item we want"`, then we will `.append()` that item to our previously empty list.

empty_list = []
for item in collection:
    if item == "item we want":
        empty_list.append(item)

Check it out!

empty_list

To iterate through the list `diseases` and make a new list with only the items that match `"recent emigrant"`, we could use the same template.

diseases = ['', 'recent emigrant', 'sickness', '', '', '', 'destitution', '', 'sickness', '',
            'sickness', 'recent emigrant', '', 'insane', 'recent emigrant', 'insane', '', '',
            'sickness', 'sickness', '', 'syphilis', 'sickness', '', 'recent emigrant', 'destitution',
            'sickness', 'recent emigrant', 'sickness', 'sickness']

recent_emigrants = []
for disease in diseases:
    if disease == 'recent emigrant':
        recent_emigrants.append(disease)

recent_emigrants

How many items are in this list? Remember that we can use the `len()` function to see how many items are in a list.

len(recent_emigrants)

We could also create a new list that revises the old list and transforms blank values into more informative values.

Below we are iterating through the list `diseases`. If an item is blank, then we are adding`"no disease recorded"` to a new `updated_diseases` list. If an item is not blank, we are simply adding the `disease` to the new list.

updated_diseases = []
for disease in diseases:
    if disease == '':
        new_disease = 'no disease recorded'
        updated_diseases.append(new_disease)
    else:
        updated_diseases.append(disease)

updated_diseases

## List Comprehensions

There's a slightly easier and more compact way to build a list with a `for` loop called a *list comprehension*.


````{list-table}
:header-rows: 1

* - Loop
  - List Comprehension
* - ```
    empty_list = []
    for item in collection:
        if item == "item we want":
            empty_list.append(item)
    ```
  - ```
    empty_list = [item for item in collection if item == 'item we want']
    ```
````

Instead of creating an empty list, you can build the `for` loop inside of a list, and you can do it all in one line.

Rather than this...

empty_list = []
for item in collection:
    if item == "item we want":
        empty_list.append(item)

We can do this...

empty_list = [item for item in collection if item == 'item we want']

empty_list

You might think of a list comprehension unfolding in the following order: "the item we want to extract" followed by a flattened `for` loop. 

To make the list `recent_emigrants` with a list comprehension, for example, we start with `disease` — that is, the "item we want to extract" — and followed it up with a flattened `for` loop.

recent_emigrants = [disease for disease in diseases if disease == 'recent emigrant']

recent_emigrants

There's no significant difference between the 4-line `for` loop and the 1-line list comprehension, except that the list comprehension is easier to write (once you get the hang of it) and takes up less space.

## Zip Lists Together

We can also iterate through multiple lists at the same time by using the `zip()` function, which basically "zips" the lists together.

first_names = ['Unity', 'Catherine', 'Thomas', 'William', 'Patrick', 'Mary Anne', 'Morris',
               'Michael', 'Ellen', 'James', 'Michael', 'Hannah', 'Alexander', 'Mary A', 'Serena?',
               'Margaret', 'Michael', 'Jane', 'Rosanna', 'James', 'Michael', 'John', 'John', 'Mary',
               'Bantel', 'Marcella', 'Arthur', 'Michael', 'Mary', 'Martin']

last_names =  ['Harkin', 'Doyle', 'McDonald', 'Jordan', 'Rouse', 'Keene', 'Brown',
               'McLoughlin', 'Cassidy', 'Whittle', 'Coyle', 'Cullen', 'Cozens', 
               'Maly', 'McGuire', 'Laly', 'Bahan', 'Combs', 'McGovern', 'Gallagher', 
               'Crone', 'Brannon', 'McDonal', 'Atkins', 'Garragan', 'Wood', 'Kelly', 'Galeny', 'Welch', 'Kerly']

updated_diseases

ages = ['22', '21', '23', '47', '45', '28', '23', '50', '26', '28', '30', '30', '65', '17', '35',
        '27', '32', '40', '22', '30', '27', '40', '41', '37', '16', '20', '30', '30', '35', '9']

For example, if we wanted to print out each Bellevue Almshouse patient's first name and their "disease" as recorded by the NYC government, we could `zip()` the lists together and unpack multiple variables.

for first_name, disease in zip(first_names, updated_diseases):
    print(f"{first_name} // {disease}")

for first_name, last_name, age, disease in zip(first_names, last_names, ages, updated_diseases):
    print(f"{first_name} {last_name} // Age {age} // {disease}")

If you try to `zip()` a list that is a different length than the other lists, it will only zip to the length of the shortest list.

another_list = ['laborer']

for first_name, last_name, age, disease, list_item in zip(first_names, last_names, ages, updated_diseases, another_list):
    print(f"{first_name} {last_name} // Age {age} // {disease} // {list_item}")

## Count Items In a List or Collection

If you want to count the items in a list or a collection, you can use the `Counter` module from the `collections` library. 

To use this tool, you first need to `import` it. The `import`statement is used whenever you want to import an external Python package or library that was written by someone else.

The `from` keyword allows us to `import` a specific module from a larger library — in this case, from `collections`.

from collections import Counter

Now that we have `Counter` imported, we can use it. To count the items in a collection, we simply need to insert a collection inside the `Counter()` function.

Counter(updated_diseases)

This gives us another kind of a collection called a *dictionary*, which we will discuss in a later lesson. This dictionary includes every item in the list and how many times it appears in the list.

#### Most Common

 To sort this Counter dictionary based on the most commonly occurring items, we can use the `.most_common()` method.

disease_tally = Counter(updated_diseases)
disease_tally.most_common()

We can also select a certain number of the top most common items by placing a number inside the `.most_common()` method.

disease_tally.most_common(2)

#### Least Common

We can also select a certain number of the *least* common items by extracting a slice from the end of list.

disease_tally.most_common()[-2:]

```{admonition}
:class: pythonreview
For a refresher on how to slice from the end of a list, see list slices in the previous lesson.
```

## Exercises

shuffled_professions = ['married', 'married', 'laborer', 'laborer', 'widow', 'married', 'spinster',
                     'laborer', 'spinster', 'laborer', 'spinster', 'spinster', 'married', 'laborer',
                     'laborer', 'spinster', 'laborer', 'laborer', 'laborer', 'laborer', 'laborer', 'spinster',
                     'laborer', 'spinster', 'widow', 'spinster', 'painter', 'laborer', 'weaver', 'laborer']

### Exercise 1

Make a new list that includes only the items in the list `shuffled_professions` that matches `spinster`

#Your code here
#Your code here
    #Your code here
        #Your code here

### Exercise 2

Print out each item in the list `shuffled_professions` next to an index number 

#Your code here
    #Your code here

### Exercise 3

Find the most and least common diseases in the list `shuffled_professions`

#Your code here