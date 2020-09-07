# Files & Character Encoding

## Open a Text File

If you want to read or write a text file with Python, it is necessary to first open the file. To open a file, you can use Python's built-in `open()` function.

open('sample-file.txt', encoding='utf-8')

Inside the `open()` function parentheses, you insert the filepath to be opened in quotation marks. You should also insert a character encoding, which we will talk more about below. This function returns what's called a *file object*.

## Read a Text File

A file object does not contain readable text. To read this file object as text, you need to use the `.read()` method. 

open('sample-file.txt', encoding='utf-8').read()

## Write a Text File

The default mode for the `open()` function is to read text files: `mode = 'r'`.

But you can use the `open()` function to write files, too. Simply set the mode to write: `mode = 'w'`

open('a-new-file.txt', mode='w', encoding='utf-8')

To write something to this newly opened text fle, you can use the `.write()` method.

open('a-new-file.txt', mode='w', encoding='utf-8').write('I just wrote this to a text file. Alright!')

If we read this newly created text file, we can see that the `.write()` method worked correctly:

open('a-new-file.txt', mode='r', encoding='utf-8').read()

## Character Encoding

encoding='utf-8'

Why do we need to include `encoding='utf-8'` to open our text file? Well, UTF-8 is a character encoding (a specific kind of [Unicode](https://home.unicode.org/basic-info/faq/)). We need to specify a character encoding because — *gasp!* — computers don't actually know what text is. Character encodings are systems that map characters to numbers. Each character is given a specific ID number. This way, computers can actually read and understand characters.

You can check any characters' "code point," or place in the Unicode universe, with the function `ord()`

ord("a")

ord("💩")

ord("ত")

ord("!")

Unicode is the most popular character encoding on the internet. It even includes emojis. Yet, as Aditya Mukerjee points out in his essay "[I Can Text You A Pile of Poo, But I Can’t Write My Name](https://modelviewculture.com/pieces/i-can-text-you-a-pile-of-poo-but-i-cant-write-my-name)", Unicode still does not include characters that are essential to the Bengali alphabet as well as to many other non-English languages.

## Adding (UTF-8) Encoding

It's always good practice to explicitly specify UTF-8 encoding when opening files.

sample_text_default = open('sample-character-encoding.txt', encoding='utf-8').read()
print(sample_text_default)

Look what happens if we read in the exact same text with a different encoding.

sample_text_iso = open('sample-character-encoding.txt', encoding='iso-8859-1').read()
print(sample_text_iso)

sample_text_ascii = open('sample-character-encoding.txt', encoding='ascii').read()
print(sample_text_ascii)

## Debugging Tip

If you're trying to read or analyze a text file, and it looks kind of weird, it's likely an encoding error: 

sample_text_iso = open('sample-character-encoding.txt', encoding='iso-8859-1').read()
print(sample_text_iso)

As David C. Zentgraf writes in his useful blog post about [character encoding](http://kunststube.net/encoding/):

> If you open a document and it looks like this [see garbled stuff above], there's one and only one reason for it: Your text editor, browser, word processor or whatever else that's trying to read the document is assuming the wrong encoding. That's all. The document is not broken...there's no magic you need to perform, you simply need to select the right encoding to display the document.

No magic! Just double check the encoding.

## More Advanced: Open and Read All Files in a Directory

We haven't fully discussed Python modules and for loops yet, but once you're comfortable with these concepts, it's helpful to know how to work with all the files in a directory.

**Import Path library**

from pathlib import Path

directory_path = 'sample-directory'

**Loop through any file in the directory with the star `*` character, which matches anything**

for filepath in Path(directory_path).glob('*'):
    print(filepath)

**Loop through just text files in the directory with `*.txt`, which matches only files that end with ".txt"**

for filepath in Path(directory_path).glob('*.txt'):
    print(filepath)

**To read these text files, simply add in the `open()` function and `.read()` method**

for filepath in Path(directory_path).glob('*.txt'):
    print(open(filepath, encoding='utf-8').read())