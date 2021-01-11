# String Methods

A *string* is a Python data type that is treated like text, even if it contains a number. Strings are always enclosed by either single quotation marks `'this is a string'` or double quotation marks `"this is a string"`. In this lesson, we're going to explore some special things that you can do with strings.

## Practice with Strings

We're going to practice by using Franz Kafka's 1915 novella, *The Metamorphosis.*

sample_text = open("../texts/literature/Kafka-The-Metamorphosis.txt", encoding="utf-8").read()

print(sample_text)

## Extract Parts of Strings

### Index

By using square brackets `[]`, you can grab or "index" part of a string based on its character number.

Here's what happens if we index the first few characters of the *The Metamorphosis*. Remember that its opening line reads: "One morning, when Gregor Samsa woke from troubled dreams."

```{admonition} Python Review
:class: pythonreview
A Python index begins with `0`. So the `0`th character in a Python string is actually the `1`st character.
```

sample_text[0]

sample_text[1]

sample_text[2]

### Slice

You can slice a string up between certain characters or up to certain characters.

string[start:stop:step]

By putting specific index numbers between these colons, you can slice the string  at certain starting and stopping points, and you can also "step" by different amounts—that is, you can jump by a certain number through the string and take every nth item in the string (e.g. every 3rd item).

Let's index our Kafka sample text from the beginning to the 121st character.

sample_text[:121]

sample_text[0:121]

Let's index our Kafka sample text from the 121st character to the 250th character.

sample_text[121:250]

Let's create a varaible `first_line` and assign it the first sentence of *The Metamorphosis*.

first_line = sample_text[:121]
print(first_line)

## String Methods

| **String Method** | **Explanation**                                                                                   |
|:-------------:|:---------------------------------------------------------------------------------------------------:|
| `string.lower()`         | makes the string lowercase                                                                                |
| `string.upper()`         | makes the string uppercase  
| `string.title()`         | makes the string titlecase 
| `string.strip()`         | removes lead and trailing white spaces     |
| `string.replace('old string', 'new string')`      | replaces `old string` with `new string`          |
| `string.split('delim')`          | returns a list of substrings separated by the given delimiter |
| `string.join(list)`         | opposite of split(), joins the elements in the given list together using the string                                                                        |
| `string.startswith('some string')`       | tests whether string begins with `some string` |                                                       |
| `string.endswith('some string')`       |  tests whether string ends with `some string`   |
| `string.isspace()`       |  tests whether string is a space |

                                                            

## Replace Words

| **String Method** | **Explanation**                                                                                   |
|:-------------:|:---------------------------------------------------------------------------------------------------:|
| `string.replace('old string', 'new string')`      | replaces `old string` with `new string`          |
                                                            

To replace a certain string within a string, you can used the `replace` method. 

print(first_line.replace("morning", "evening"))

print(first_line.replace("vermin", "grilled cheese"))

Your turn! Replace the word "vermin" with a word of your choosing:

first_line.replace("vermin", #your code here )

## Transform Strings to Lowercase/Uppercase

| **String Method** | **Explanation**                                                                                   |
|:-------------:|:---------------------------------------------------------------------------------------------------:|
| `string.lower()`         | makes the string lowercase                                                                                |
| `string.upper()`         | makes the string uppercase  
| `string.title()`         | makes the string titlecase 

("I am really very quiet").lower()

("I am really very quiet").upper()

Your turn! Transform the first line of Kafka's *The Metamorphosis* to upper case:

# your code here

## Split Strings By a Delimiter

| **String Method** | **Explanation**                                                                                   |
|:-------------:|:---------------------------------------------------------------------------------------------------:|
| `string.split('delim')`          | returns a list of substrings separated by the given delimiter |                                                       

With the `.split()` method, you can split up a strings into a a list of parts. By default, it splits on spaces, but you can put in a different delimiter and split on something else. 

first_line.split()

Your turn! Split on the words "dreams" and see what happens.

# your code here

## Join Strings By a Delimiter

| **String Method** | **Explanation**                                                                                   |
|:-------------:|:---------------------------------------------------------------------------------------------------:|
| `string.join(list)`         | opposite of split(), joins the elements in the given list together using the string                           
                                                            

You can also put something back together again with the `join()` method!

kafka_split_words = first_line.split()
kafka_split_words

"SPACE".join(kafka_split_words)

" ".join(kafka_split_words)

Your turn! Join `kafka_split_words` with a delimiter of your choosing.

# your code here