# Common Python Errors

Below are a few common error messages that you will likely encounter as you first learn Python and long afterward. No matter how much you know, you will always encounter errors!

To learn more about these and other Python errors, see [Python's official documentation](https://docs.python.org/3/library/exceptions.html#bltin-exceptions).

## SyntaxError

A `SyntaxError` means that something has gone wrong with your Python syntax, aka the arrangement of words and punctuation in your code. Often, as below, this error will result from forgetting a closing quotation mark in a string or from forgetting a colon in a `for` loop. 

print("Hope this goes off without a hitch!)

for item in items
    print(item)

The error message will often include a caret or arrow that points to the problematic part of the code:

## FileNotFound Error

A `FileNotFoundError` means that whatever file name you've typed in cannot be located. Often, this error will result from simple typos in the file name or from not pointing to the correct directory which contains the file. Double check your spelling and where your desired file is located relative to your Python code.

open('../Wrong-Directory/File-Name.txt').read()

## TypeError

A `TypeError` means that you're trying to perform a function or operation on something that is not the correct data type for that function or operation. For example, if you try to divide by a variable that is a string, rather than an integer or float (as in the example below), a `TypeError` will be thrown. Double check your data types with the `type()` function.

favorite_artist = "Beyoncé"

favorite_artist / 2

type(favorite_artist)

## NameError

A `NameError` means that the variable name that you're using cannot be found. Often, this error results from forgetting to run the cell that defines your variable or from misspelling the name of your variable, as below. Check your spelling and make sure you've run all necessary cells.

favorite_artist = "Beyoncé"

favorite_arteest

## AttributeError

An `AttributeError` means that you're trying to access something from an object that that object doesn't possess or do something with an object that that object cannot do. For example, to transform the variable `favorite_artist` (which contains the string "Beyoncé") from title case to uppercase, we can run `favorite_arist.upper()` because `.upper()` is a built-in string method. But if we forget the name of that string method and instead type `.uppercase()`, which is not an existing string method, then an `AttributeError` will be raised.

favorite_artist.upper()

favorite_artist.uppercase()