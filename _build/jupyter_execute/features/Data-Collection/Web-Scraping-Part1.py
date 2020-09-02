# Web Scraping — Part 1

*Inspired by web scraping lessons from [Lauren Klein](https://github.com/laurenfklein/emory-qtm340/blob/master/notebooks/class4-web-scraping-complete.ipynb) and [Allison Parrish](https://github.com/aparrish/dmep-python-intro/blob/master/scraping-html.ipynb)*

In this series of lessons, we're going to introduce how to "scrape" data from the internet with the Python libraries requests and BeautifulSoup.

We will cover how to:

* Programmatically access the text of a web page
* Understand the basics of HTML
* Extract certain HTML elements

## Why Do We Need To Scrape At All?

To understand the significance of web scraping, let's walk through the likely data collection process behind [“Film Dialogue from 2,000 screenplays, Broken Down by Gender and Age”](https://pudding.cool/2017/03/film-dialogue/).

To find their 2,000 screenplays, Hannah Andersen and Matt Daniels consulted a number of already existing sources — one of which was the [Cornell Movie Dialogues Corpus](http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html). This is a corpus created by Cornell CIS professors Cristian Danescu-Niculescu-Mizil and Lillian Lee for their paper ["Chameleons in imagined conversations"](http://www.cs.cornell.edu/~cristian/papers/chameleons.pdf). Go Big Red!

These researchers helpfully shared a dataset of every URL that they used to find and access the screenplays in their own project.

**Import Pandas**

import pandas as pd

**Read in CSV file**

urls = pd.read_csv("../data/cornell-movie-corpus/raw_script_urls.csv", delimiter='\t', encoding='utf=8')

**Display DataFrame**

urls

Each movie title in this CSV file is paired with a URL for the screenplay. How can we actually use these URLs to get computationally tractable text data?

Though we could manually navigate to each URL and copy/paste each screenplay into a file, that would be suuuuper slow and painstaking, and we would lose crucial data in the process — information that might help us automatically distinguish the title of the movie from the screenplay itself, for example. It would be much better to programmatically access the text data attached to every URL.

## Responses and Requests

To programmatically access the text data attached to every URL, we can use a Python library called [requests](https://requests.readthedocs.io/en/master/).

When you type in a URL in your search address bar, you're sending an HTTP **request** for a web page, and the server which stores that web page will accordingly send back a **response**, some web page data that your browser will render.

<img src="../images/request-response.png" class="center">

### Import Requests 

import requests

### Get HTML Data

With the `.get()` method, we can request to "get" web page data for a specific URL, which we will store in a varaible called `response`.

response = requests.get("http://www.scifiscripts.com/scripts/Ghostbusters.txt")

### HTTP Status Code

If we check out `response`, it will simply tell us its [HTTP response code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status), aka whether the request was successful or not.

"200" is a successful response, while "404" is a common "Page Not Found" error.

response

Let's see what happens if we change the title of the movie from *Ghostbusters* to *Ghostboogers* in the URL...

bad_response = requests.get("http://www.scifiscripts.com/scripts/Ghostboogers.txt")

bad_response

<img src="../images/Ghostboogers.png" class="center" >

### Extract Text From Web Page

To actually get at the text data in the reponse, we need to use `.text`, which we will save in a variable called `html_string`. The text data that we're getting is formatted in the HTML markup language, which we will talk more about in the BeautifulSoup section below.

html_string = response.text

Here's the screenplay now in a variable.

print(html_string)

### Extract Text From Multiple Web Pages

Let's quickly demonstrate how we might extract the screenplay text for every URL in the DataFrame. To do so, we're going to create a smaller DataFrame from the Cornell Movie Dialogue Corpus, which consists of the first 10 movies.

sample_urls = urls[:10]

sample_urls

We're going to make a function called `scrape_screenplay()` that includes our `requests.get()` and `response.text` code.

def scrape_screenplay(url):
    response = requests.get(url)
    html_string = response.text
    return html_string

Then we're going apply it to the "script_url" column of the DataFrame and create a new column for the resulting extracted text.

sample_urls['text'] = sample_urls['script_url'].apply(scrape_screenplay)

sample_urls

The DataFrame above is truncated, so we can't see the full contents of the "text" column. But if we print out every row in the column, we can see that we successfully extracted text for each URL (though some of these URLs returned 404 errors).

for text in sample_urls['text']:
    print(text)

## Web Scraping

Not all web pages will be as easy to scrape as these screenplay files, however. Let's say we wanted to scrape the lyrics for Missy Elliott's song "The Rain (Supa Dupa Fly)" (1997) from Genius.com.

<img src="../images/Missy-Elliott.png" class="center" >

Even at a glance, we can tell that this *Genius* web page is a lot more complicated than the *Ghostbusters* page and that it contains a lot of information beyond the lyrics.

Sure enough, if we use our requests library again and try to grab the data for this web page, the underlying data is much more complicated, too.

response = requests.get("https://genius.com/Missy-elliott-the-rain-supa-dupa-fly-lyrics")
html_string = response.text
print(html_string)

How can we extract just the song lyrics from this messy soup of a document? Luckily there's a Python library that can help us called BeautifulSoup, which parses HTML documents.

To understand BeautifulSoup and HTML, we're going to briefly depart from our Missy Elliot lyrics challenge to consider a much simpler website. This toy website was made by the poet, programmer, and professor Allison Parrish explicitly for the purposes of teaching BeautifulSoup.

## HTML

Parrish's website is titled "Kittens and the TV Shows They Love." It can be found at the following URL: http://static.decontextualize.com/kittens.html

<img src="../images/kittens-web.png" class="center" >

If we use our requests library on this Kittens TV website, this is what we get:

response = requests.get("http://static.decontextualize.com/kittens.html")
html_string = response.text
print(html_string)

### HTML Tags

This is an HTML document. HTML stands for HyperText Markup Language. It is the standard language for writing web page documents. The most important thing you need to know about HTML is that the language uses HTML "tags" to represent different elements, such as a main header `<h1>`. 

| HTML Tag                | Explanation                              |
|--------------------|-------------------------------------------|
| <\!DOCTYPE>        | Defines document type                 |
| <html\>             | Defines HTML document                  |
| <head\>             | Main information about document    |
| <title\>            | Title for document          |
| <body\>             | Document body               |
| <h1\> to <h6\>       |  Headings                    |
| <p\>                | Paragraph                       |
| <br\>               | Line break               |
| <\!\-\-comment here-\-> | Comment                         |
| <img\> | Image                         |
| <a\> | Hyperlink                       |
| <ul\> | Unordered list                     |
| <ol\> | Ordered list                     |
| <li\> | List item                     |
| <style\> | Style information for a document                    |
| <div\> | Section in a document                   |
| <span\> | Section in a document                   |

HTML tags often, but not always, require a "closing" tag. For example, the main header "Kittens and the TV Shows They Love" will be surrounded by `<h1>` (opening tag) and `</h1>` (closing tag) on either side: `<h1>Kittens and the TV Shows They Love</h1>`

### HTML Attributes, Classes, and IDs

HTML elements sometimes come with even more information inside a tag. This will often be a keyword (like `class` or `id`) followed by an equals sign `=` and a further descriptor such as `<div class="kitten">`

We need to know about tags as well as attributes, classes, and IDs because this is how we're going to extract specific HTML data with BeautifulSoup.

## BeautifulSoup

from bs4 import BeautifulSoup

To make a BeautifulSoup document, we call `BeautifulSoup()` with two parameters: the `html_string` from our HTTP request and [the kind of parser](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#specifying-the-parser-to-use) that we want to use, which will always be `"html.parser"` for our purposes.

response = requests.get("http://static.decontextualize.com/kittens.html")
html_string = response.text

document = BeautifulSoup(html_string, "html.parser")

document

### Extract HTML Element

We can use the `.find()` method to find and extract certain elements, such as a main header.

document.find("h1")

If we want only the text contained between those tags, we can use `.text` to extract just the text.

document.find("h1").text

type(document.find("h1").text)

Find the HTML element that contains an image.

document.find("img")

### Extract Multiple HTML Elements

You can also extract multiple HTML elements at a time with `.find_all()`

document.find_all("img")

document.find_all("div", attrs={"class": "kitten"})

document.find("h2").text

document.find_all("h2")

```{error}
The code below will cause an error.
```

Let's try to extact the text from all the header2 elements:

document.find_all("h2").text

Uh oh. That didn't work! In order to extract text data from multiple HTML elements, we need a `for` loop and some list-building.

all_h2_headers = document.find_all("h2")

all_h2_headers

First we will make an empty list called `h2_headers`.

Then `for` each `header` in `all_h2_headers`, we will grab the `.text`, put it into a variable called `header_contents`, then `.append()` it to our `h2_headers` list.

h2_headers = []
for header in all_h2_headers:
    header_contents = header.text
    h2_headers.append(header_contents)

h2_headers

````{admonition} Python Review: List Comprehensions
:class: pythonreview
How might we transform this for loop into a *list comprehension*?
```
#For Loop
h2_headers = []
for header in all_h2_headers:
    header_contents = header.text
    h2_headers.append(header_contents)
```
````

**Check out the *list comprehension* answer here**

h2_headers = [header.text for header in all_h2_headers]
h2_headers

## Inspect HTML Elements with Browser

Most times if you're looking to extract something from an HTML document, it's best to use your "Inspect" capabilities in your web browser. You can hover over elements that you're interested in and find that specific element in the HTML.

<img src="../images/inspect.png" class="center">

For example, if we hover over the main header:

<img src="../images/inspect-h1.png" class="center" >

## Your Turn!

Ok so now we've learned a little bit about how to use BeautifulSoup to parse HTML documents. So how would we apply what we've learned to extract Missy Elliott lyrics?

response = requests.get("https://genius.com/Missy-elliott-the-rain-supa-dupa-fly-lyrics")
html_str = response.text

document = BeautifulSoup(html_str, "html.parser")

document

https://genius.com/Missy-elliott-the-rain-supa-dupa-fly-lyrics

What HTML element do we need to "find" to extract the song lyrics?

**Check answer here**

missy_lyrics = document.find("p").text
print(missy_lyrics)

What HTML element do we need to "find" to extract the title?

**Check answer here**

song_title = document.find('h1').text
print(song_title)