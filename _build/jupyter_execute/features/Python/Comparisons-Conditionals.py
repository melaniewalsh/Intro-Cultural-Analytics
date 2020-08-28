# Comparisons & Conditionals

Writing Python code is a lot like writing a list of detailed instructions to the computer. Most of the time you will be asking the computer to perform certain tasks if certain conditions are met. For example:

- *If a person in the dataset is older than 30, then print out their name*
- *If a tweet contains the phrase "ok boomer," then automatically retweet it*
- *If Beyoncé is a Grammy award-winner, then say "Congratulations, Beyoncé!*

Here's how we would write out this last example in Python code:

beyonce = "Grammy award-winner"

if beyonce == "Grammy award-winner":
    print("Congratulations, Beyonce!")

There are two important Python elements present in the code above: a *comparison* and a *conditional*. We compared whether the variable `beyonce` is equal to the value `"Grammy award-winner"`. Then we printed "Congratulations" if this condition was `True`.

## Comparisons

There are many ways that we can compare values with Python, such as equals (`==`), not equals (`!=`), greater than (`>`), less than (`<`), greater than or equal to (`>=`), or less than or equal to (`<=`).

| **Comparison Operator** | **Explanation**                                                                                   |
|:-------------:|:---------------------------------------------------------------------------------------------------:|
| `x == y `         | `True` if x is equal to y                                                                                |
| `x != y `         | `True` if x is not equal to y                                               |
| `x > y`       |  `True` if x is greater than y                                                        |
| `x < y`       |   `True` if x is less than y  
| `x >= y`       |   `True` if x is greater than or equal to y |
| `x <= y`      | `True` if x is less than or equal to y`                                                                             |
                                                                      
                                                           

### Greater Than

Is the variable `person1` greater than `person1`?

person1 = 30
person2 = 30.5
person1 > person2

### Not Equals

Is the variable `person1` not equal to `person1`?

person1 = 30
person2 = 30.5
person1 != person2

We can also combine values and compare them. We can check to see if `x and y` are both `True` or if either `x or y` is `True`.

| **Logical Operator** | **Explanation**                                                                                   |
|:-------------:|:---------------------------------------------------------------------------------------------------:|
| `x and y`         | `True` if x and y are both True                                                                             |
| `x or y`         | `True` if either x or y is True                                              |
| `not x`       |  `True` if is x is not True                                                       |
                                                            

### And

What will happen if we check whether `person1 > 30` and `person2 > 30`?

person1 = 30
person2 = 30.5
person1 > 30 and person2 > 30

The boolean answer is `False` because `person1` is not greater than 30 (`person1` is exactly 30) even though `person2` is greater than 30. The `and` requires that both conditions are `True.` 

person1 = 30
person2 = 30.5
person1 >= 30 and person2 >= 30

The boolean answer is `True` because `person1` is greater than or equal to 30 and `person2` is greater or equal to  30. The `and` requires that both conditions are `True.` 

### Or

What will happen if we check whether `person1 > 30` or `person2 > 30`?

person1 = 30
person2 = 30.5
person1 > 30 or person2 > 30

The boolean answer is `True` because `person2` is greater than 30. The `or` requires that only one of the conditions is true.

## Conditionals

### If Statement

An `if` statement is an instruction to do something *if* a particular condition is met.

A common conditional will consist of two lines: 
- On the first line, you type the English word `if` followed by an expression and then a colon (`:`) 
- On the second line, you indent and write an instruction or "statement" to be completed if the condition is met

beyonce = "Grammy award-winner"

if beyonce == "Grammy award-winner":
    print("Congratulations, Beyonce!")

Python is picky about how you format `if` statements. Look what happens if we forget to tab over on the second line or if we forget the colon:

if beyonce == "Grammy award-winner":
print("Congratulations, Beyonce!")

if beyonce == "Grammy award-winner"
    print("Congratulations, Beyonce!")

## Else Statement

You can add even more complexity in a conditional by adding an `else` statement. This will instruct the program to do something in case the condition is not met. An `else` comes after an `if` statement and should be formatted it the same way.

beyonce = "not a Grammy award-winner this year"

if beyonce == "Grammy award-winner":
    print("Congratulations, Beyonce!")
else:
    print("They messed up, Beyonce.")

## Elif Statement

Sometimes you want even more nuance to respond to slightly different conditions. For example, if Beyonce was nominated for a Grammy but didn't win, then we might want to express a slightly different sentiment than if she won or was not nominated at all.

You can add in this nuance with an `elif` statement, short for *else if*. The computer will evaluate the first `if` statement. If that statement is not `True`, it will then evaluate the `elif` statement.

beyonce = "Grammy award-nominee"

if beyonce == "Grammy award-winner":
    print("Congratulations, Beyonce!")
elif beyonce == "Grammy award-nominee":
    print("Ok well at least they nominated you, Beyonce.")
else:
    print("They messed up, Beyonce.")

## Excerises

For the following exercises and the next few lessons, we're going to draw on Anelise Shrout's [Bellevue Almshouse Dataset](https://www.nyuirish.net/almshouse/the-almshouse-records/). The Bellevue Almshouse Dataset includes information about Irish-born immigrants who were admitted to the almshouse in the 1840s.

The Bellevue Almshouse was part of New York City's public health system, a place where poor, sick, homeless, and otherwise marginalized people were sent — sometimes voluntarily and sometimes forcibly. Devastated by widespread famine in Ireland, many Irish people fled their homes for New York City in the 1840s, and many of them ended up in the Bellevue Almshouse. This dataset was transcribed from the almshouse's own admissions records.

import pandas
pandas.read_csv("../data/bellevue_almshouse_modified.csv").head(20)

We're using the Bellevue Almshouse Dataset to practice `if`, `elif`, and `else` statements because we want to think deeply about the consequences of reducing human life to data and evaluating "Truth" in Pythonic terms even at this early stage in our Python journey.

As Shrout argues in her essay ["(Re)Humanizing Data: Digitally Navigating the Bellevue Almshouse,"](https://crdh.rrchnm.org/essays/v01-10-(re)-humanizing-data/) "Nineteenth-century immigration data was produced with the express purpose of reducing people to bodies; bodies to easily quantifiable aspects; and assigning value to those aspects which proved that the marginalized people to who they belonged were worth less than their elite counterparts."

As you complete the exercises below, reflect about the categories that these Irish immigrants were slotted into by the government. For example, the so-called "disease" that many of the people in this dataset exhibited — the reason they were admitted to the Almshouse in the first place — is "recent emigrant." What does this uncomfortable fact tell us about data more broadly? What should we make of the fact that Python, as a programming language, doesn't understand the meaning or historical context of this data?

### Exercise 1

person1_name = 'Mary Gallagher'
person1_age = 28
person1_disease = 'recent emigrant'
person1_profession = 'married'
person1_gender = 'f'
person1_child_status = 'Child Alana 10 days'

Write an `if` statement that reports whether `person1_age` is less than 30 years old

#Your code here
    print('Person is less than 30 years old.')

### Exercise 2
Write an `if` statement that reports whether `person1_profession` is "married"

#Your code here
    print('Person is married.')

### Exercise 3
Write an `if` statement that reports whether `person1_age` is less than 30 years old *and* `person1_profession` is "married"

#Your code here
    print('Person is less than 30 years old and married.')

### Exercise 4

person2_name = 'Anthony Clark'
person2_age = 60
person2_disease = 'recent emigrant'
person2_profession = 'laborer'
person2_gender = 'm'
person2_child_status = 'Charles Riley afed 10 days'

Combine an`if` statement with an `else` statement that will report whether `person2_age` is less than 30 years old or, if not, more than 30 years old

#Your code here
    print('Person is less than 30 years old.')
#Your code here
    print('Person is more than 30 years old.')

### Exercise 5

person3_name = 'Margaret Farrell'
person3_age = 30
person3_disease = 'recent emigrant'
person3_profession = 'widow'
person3_gender = 'w'
person3_child_status = ''

Add an `elif` statement that reports whether `person3_age` is exactly 30 years old

#Your code here
    print('Person is less than 30 years old.')
#Your code here
    print('Person is exactly 30 years old.')
#Your code here
    print('Person is more than 30 years old.')

### Exercise 6

person1_child_status = 'Child Alana 10 days'
person3_child_status = ''

Write an `if` statement that will report whether `person1_child_status` includes children

#Your code here
    print('Person has children.')

### Exercise 7
Write a single `if` statement that will accurately report whether `person1_child_status` includes children and if `person3_child_status` includes children

```{hint}
:class: dropdown
Think about how you might use the `!=` operator!  

And remember that there's a difference between quotation marks with no space `''` and quotation marks with a space`' '`. Python is picky!
```

if person1_child_status #Your Code Here
    print('Person has children.')

if person2_child_status #Same Code Here
    print('Person has children.')

### Excerise 8

person1_profession = 'married'

Write a conditional that will report whether `person1_profession` is "married," "laborer," "widow," or "unknown profession." Then test your code by reassigning the variable as indicated below.

#Your code here
    print('Person is married.')
#Your code here
    print('Person is a laborer.')
#Your code here
    print('Person is a widow.')
#Your code here
    print('Person has unknown profession.')

person1_profession = 'laborer'

#Your code here
    print('Person is married.')
#Your code here
    print('Person is a laborer.')
#Your code here
    print('Person is a widow.')
#Your code here
    print('Person has unknown profession.')

person1_profession = 'student'

#Your code here
    print('Person is married.')
#Your code here
    print('Person is a laborer.')
#Your code here
    print('Person is a widow.')
#Your code here
    print('Person has unknown profession.')

### Exercise 9

person4_name = 'John Sanin(?)'


Some of the Irish immigrants' names have question marks after them. Let's clean up some of the data and remove the question marks.

You can use the Python keyword `in` to test whether a string appears within another string. Print `person4_name` with the question mark and parentheses removed. 
```{hint}
:class: dropdown
Remember the string method `.replace()`?

if "(?)" in person2_name:
    #Your code here

### Exercise 10
In a few sentences, discuss the following dilemma. Python doesn't understand the historical context or human meaning behind data. What consequences might this incomprehension have on our society? How can we be sure to preserve the historical context and human meaning behind data when we are working with Python?

**Double-click this cell to type your thoughts here**