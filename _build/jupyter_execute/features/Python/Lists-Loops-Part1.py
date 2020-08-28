# Lists & Loops — Part 1

In the next few lessons, we're going to learn about a Python data collection type called a *list* and a way of working with lists called a *for loop*, and we're going to draw on [The Bellevue Almshouse Dataset](https://www.nyuirish.net/almshouse/the-almshouse-records/), created by historian and DH scholar Anelise Shrout. This dataset includes information about Irish-born immigrants who were admitted to New York City's Bellevue Almshouse in the 1840s. 

**Preview The Bellevue Almshouse Dataset**

import pandas
pandas.read_csv("../data/bellevue_almshouse_modified.csv").head(20)

```{margin} The Bellevue Almshouse Dataset 
The Bellevue Almshouse Dataset includes information about Irish-born immigrants who were admitted to the almshouse in the 1840s. The Bellevue Almshouse was part of New York City's public health system, a place where poor, sick, homeless, and otherwise marginalized people were sent — sometimes voluntarily and sometimes forcibly. This dataset was transcribed from the almshouse's own admissions records by Anelise Shrout.
```

We're using the [Bellevue Almshouse](https://www.nyuirish.net/almshouse/the-almshouse-records/) data to practice lists and loops because we want to think deeply about the consequences of reducing human life to data, even at this early stage in our Python journey. This immigration data, as Shrout argues in her essay ["(Re)Humanizing Data: Digitally Navigating the Bellevue Almshouse,"](https://crdh.rrchnm.org/essays/v01-10-(re)-humanizing-data/) was "produced with the express purpose of reducing people to bodies; bodies to easily quantifiable aspects; and assigning value to those aspects which proved that the marginalized people to who they belonged were worth less than their elite counterparts."

As we work through the lesson below, reflect about the categories that these Irish immigrants were slotted into by the NYC government. What should we make of the fact that Python, as a programming language, doesn't understand the meaning or historical context of this data? How can we nevertheless use Python to better understand this history and to interrogate power?

___

## Lists

In the previous lesson, we used individual variables to represent some of the demographic information about the 19th century Irish immigrants featured in the  [Bellevue Almshouse data](https://docs.google.com/spreadsheets/d/1uf8uaqicknrn0a6STWrVfVMScQQMtzYf5I_QyhB9r7I/edit##gid=2057113261), such as names.

person1_name = 'Marry Gallagher'
person2_name = 'John Sanin (?)'

It's typically more useful, however, to create a *collection* of values rather than individual variables. 

One of the most common Python data collections is a *list*. By using a list, we can put the names of the people featured in the dataset into a single collection.

names = ['Mary Gallagher', 'John Sanin(?)', 'Anthony Clark', 'Margaret Farrell']

type(names)

A list is always enclosed by square brackets `[]` and accepts items in a row separated by commas (`,`). A list can contain any combination of Python data types.

ages = [28, 19, 60, 30]

type(ages)

### Index

You can index a list like you would index a string.

names = ['Mary Gallagher', 'John Sanin(?)', 'Anthony Clark', 'Margaret Farrell']

For example, if we wanted to pull out the first item in our `names` list, we could put square brackets and our desired index number immediately after the list. Just like with strings, the Python index begins with 0.

names[0]

names[3]

You can also reverse index a list.

names[-1]

### Slice

You can also slice lists like you can slice a string.

more_names = ['Unity', 'Catherine', 'Thomas', 'William', 'Patrick',
              'Mary Anne', 'Morris', 'Michael', 'Ellen', 'James']

The full notation and options for slicing a list are as follows:

your_list[start:stop:step]

By putting specific index numbers between these colons, you can slice the list at certain starting and stopping points, and you can also "step" by different amounts—that is, you can jump by a certain number through the list and only take every nth item in the list (e.g. every 3rd item).

````{list-table}
:header-rows: 1

* - Slice 
  - Explanation
  - Output
* - ```
     more_names[:2]
     ```
  - Slice list up to 2nd item
  - ```
    ['Unity', 'Catherine']
    ```
* - ```
     more_names[2:]
     ```
  - Slice from 2nd item to end of list 
  - ```
      ['Thomas',
     'William',
     'Patrick',
     'Mary Anne',
     'Morris',
     'Michael',
     'Ellen',
     'James']
    ```
* - ```
     more_names[::3]
     ```
  - Slice from 0 to end of list, stepping by 3
  - ```
    ['Unity', 'William', 'Morris', 'James']
    ```

````

#### Start

more_names = ['Unity', 'Catherine', 'Thomas', 'William', 'Patrick',
              'Mary Anne', 'Morris', 'Michael', 'Ellen', 'James']

Here's how we would slice the list starting from the 2nd item of the list until the end.

more_names[2:]

You might imagine the above as:

more_names[start=2:stop=none:step=none]

Remember that the Python index starts with `0` so the 2nd item is really the 3rd item.

more_names[2]

#### Reverse

more_names = ['Unity', 'Catherine', 'Thomas', 'William', 'Patrick',
              'Mary Anne', 'Morris', 'Michael', 'Ellen', 'James']

Because we can reverse index a list from the end to the beginning, we can also slice a list by starting from the 2nd to last item until the end.

more_names[-2:]

You might imagine the above as:

more_names[start=-2:stop=none:step=none]

#### Stop

more_names = ['Unity', 'Catherine', 'Thomas', 'William', 'Patrick',
              'Mary Anne', 'Morris', 'Michael', 'Ellen', 'James']

Here's how we would slice the list starting from 0 and ending at the 2nd item in the list.

more_names[:2]

You might imagine the above as:

more_names[start=0:stop=2:step=none]

#### Step

You can also index by a certain number of steps.

Here's how we could index every third item in the list.

more_names[::3]

You might imagine the above as:

more_names[start=0:stop=0:step=3]

## List Methods

Lists also have a number of special methods that can be used with them, such as a method for adding items to a list.

| **List Method** | **Explanation**                                                                                   |
|-------------|---------------------------------------------------------------------------------------------------|
| `list.append(another_item)`          | adds new item to end of list                                                                                |
| `list.extend(another_list)`        | adds items from another_list to list                                                |
| `list.remove(item)`        | removes first instance of item                                                       |
| `list.sort(reverse=False)`       | sort the order of list                                                                                 |                                                     |
| `list.reverse()`       | reverses order of list                                                                                 |                                                     |

### Add Items To List

| **List Method** | **Explanation**                                                                                   |
|-------------|---------------------------------------------------------------------------------------------------|
| `list.append(another_item)`          | adds new item to end of list                                                                   

names = ['Mary Gallagher', 'John Sanin(?)', 'Anthony Clark', 'Margaret Farrell']

names.append("Lawrence Feeney")

names

### Sort List

| **List Method** | **Explanation**                                                                                   |
|-------------|---------------------------------------------------------------------------------------------------|
| `list.sort(reverse=False)`       | sort the order of list                                                                             

names.sort()

names

ages.sort()

ages

ages.sort(reverse=True)

ages

### Extend List With Another List

| **List Method** | **Explanation**                                                                                   |
|-------------|---------------------------------------------------------------------------------------------------|
| `list.extend(another_list)`        | adds items from another_list to list                                                                                 

names.extend(ages)

names

## For Loops

One of the best ways to work with a list is with `for` loops. This is a way of considering each item in the list or "iterating" through the list.

names = ['Mary Gallagher', 'John Sanin(?)', 'Anthony Clark', 'Margaret Farrell']

for name in names:
    print(name)

A basic basic `for` loop will consist of two lines:

- On the first line, you type the English word `for`, a new variable name for each item in the list, the English word `in`, the name of the list, and a colon (`:`)

- On the second line, you indent and write an instruction or “statement” to be completed for each item in the list

for name in names:
    print(f"Person's name is {name}")

for x in names:
    print(f"Person's name is {x}")

ages = [28, 19, 60, 30]

for age in ages:
    if age > 30:
        print("Person is less than 30 years old")
    else:
        print("Person is more than 30 years old")

for age in ages:
    print(age * 2)

## Exercises

professions = ['married', 'laborer', 'widow', 'laborer', ]
child_status = ['Child Alana 10 days', 'Catherine 2 mos', '', 'Charles Riley afed 10 days' ]
gender = ['f', 'm', 'w', 'm']

### Exercise 1
Extract the second item in the list `professions`.

```{hint}
:class: dropdown
Remember that the Python index begins with 0!
```

##Your Code Here

### Exercise 2
Add the item "spinster" to your `professions` list, then print the list.

##Your Code Here

##Your Code Here

### Exercise 3
Make a `for` loop that considers each item in the `professions` list and prints "Person's profession is ___"

##Your Code Here
    ##Your Code Here

### Exercise 4
Extract the fourth item in the `child_status` list.

##Your Code Here

### Exercise 5
Make a `for` loop that considers each item in the `child_status` list and prints "Person has child" if the person has a child and "Person does not have child" if not

##Your Code Here
  ##Your Code Here
       ##Your Code Here
    ##Your Code Here
        ##Your Code Here

### Exercise 6
Add an item to the list `gender` called "not known"

##Your Code Here

### Exercise 7
Make a `for` loop that considers each item in the `gender` list and prints "Person is male" if the person is male, "Person is female" if the person is female, and "Person's gender is not known" if unknown

 ##Your Code Here
     ##Your Code Here
         ##Your Code Here
     ##Your Code Here
         ##Your Code Here
     ##Your Code Here
         ##Your Code Here