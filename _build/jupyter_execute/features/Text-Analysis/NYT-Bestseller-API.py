# New York Times Bestseller API

To use any of the New York Times APIs, you will need a special API key. Getting a NYT API key is free and shouldn't take more than a few minutes.

To get your own API key, you need to sign up for a NYT Developer account, create a new "App," and then select which APIs you would like access to. Find full [start-up instructions](https://developer.nytimes.com/get-started) on the NYT Developer site.

Once you have a NYT API key, paste it into the quotation marks below.

my_api_key = "PVvQcv5ov1V9fy6cLAdJAUAo9cymw38a"

my_api_key = "PASTE-YOUR-API-KEY-BETWEEN-QUOTATION-MARKS-HERE"

import requests

import pandas as pd
pd.set_option("max_columns", 50)
pd.set_option("max_colwidth", 100)

To see which lists we can search for, we can use this API request URL:

https://api.nytimes.com/svc/books/v3/lists/names.json?api-key={my_api_key}

for nyt_list in requests.get(f"https://api.nytimes.com/svc/books/v3/lists/names.json?api-key={my_api_key}").json()['results']:
    print(nyt_list['list_name'])

list_genre = "Hardcover Fiction"

response = requests.get(f"https://api.nytimes.com/svc/books/v3/lists/current/{list_genre}.json?api-key={my_api_key}")

response.json()

json = response.json()

dataframe = pd.json_normalize(json['results']['books'])
dataframe[['rank', 'weeks_on_list','title', 'author','publisher', 'primary_isbn10', 'book_image']] 

from IPython.core.display import HTML

def get_image_html(link):
    image_html = f"<img src='{link}' width='100'>"
    return image_html

def display_images(dataframe):
    return HTML(dataframe.to_html(escape=False))

dataframe['book_cover'] = dataframe['book_image'].apply(get_image_html)

display_images(dataframe[['book_cover','rank', 'weeks_on_list','title', 'author','publisher', 'primary_isbn10']] )

list_genre = "Celebrities"

response = requests.get(f"https://api.nytimes.com/svc/books/v3/lists/current/{list_genre}.json?api-key={my_api_key}").json()

dataframe = pd.json_normalize(response['results']['books'])
dataframe['book_cover'] = dataframe['book_image'].apply(get_image_html)
display_images(dataframe[['book_cover','rank', 'weeks_on_list','title', 'author','publisher', 'primary_isbn10']] )

list_genre = "Indigenous Americans"

response = requests.get(f"https://api.nytimes.com/svc/books/v3/lists/current/{list_genre}.json?api-key={my_api_key}").json()

dataframe = pd.json_normalize(response['results']['books'])
dataframe['book_cover'] = dataframe['book_image'].apply(get_image_html)
display_images(dataframe[['book_cover','rank', 'weeks_on_list','title', 'author','publisher', 'primary_isbn10']] )

list_genre = "E-Book Fiction"

response = requests.get(f"https://api.nytimes.com/svc/books/v3/lists/current/{list_genre}.json?api-key={my_api_key}").json()

dataframe

dataframe = pd.json_normalize(response['results']['books'])
dataframe['book_cover'] = dataframe['book_image'].apply(get_image_html)
display_images(dataframe[['book_cover','rank', 'weeks_on_list','title', 'author','publisher', 'primary_isbn10']] )

