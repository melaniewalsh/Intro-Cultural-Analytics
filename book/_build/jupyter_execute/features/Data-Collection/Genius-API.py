# Song Genius API

In this lesson, we're going to use the Genius API to access data about Missy Elliott songs.

## API Keys

To use the Genius API, you need a special API key, specifically a "Client Access Token", which is kind of like a password. Many APIs require authentication keys to gain access to them. To get your necessary Genius API keys, you need to navigate to the following URL: [https://genius.com/api-clients](https://genius.com/api-clients).

<img src="../images/Genius-API.png" width=100% >

You'll be prompted to sign up for [a Genius account](https://genius.com/signup_or_login), which is required to gain API access. Signing up for a Genius account is free and easy. You just need a Genius nickname (which must be one word), an email address, and a password.

Once you're signed in, you should be taken to [https://genius.com/api-clients](https://genius.com/api-clients), where you need to click the button that says "New API Client."

<img src="../images/Genius-New-API.png" width=100% >

After clicking "New API Client," you'll be prompted to fill out a short form about the "App" that you need the Genius API for. You only need to fill out "App Name" and "App Website URL."

It doesn't really matter what you type in. You can simply put "Song Lyrics Project" for the "App Name" and the URL for our course website "https://melaniewalsh.github.io/Intro-Cultural-Analytics/" for the "App Website URL."

When you click "Save," you'll be given a series of API Keys: a "Client ID" and a "Client Secret." To generate your "Client Access Token," which is the API key that we'll be using in this notebook, you need to click "Generate Access Token".

Finally, copy and paste your "Client Access Token" into the quotation marks below, and run the cell to save your variable 

client_access_token = "INSERT YOUR CLIENT ACCESS TOKEN IN THESE QUOTATION MARKS"

### Protecting Your API Key

For this lesson, if you just copy and paste your Genius API key into your Jupyter notebook, everything should be fine. But that's actually not the best way of storing your API keys. If you published this notebook to GitHub, for example, other people might be able to read and use/steal your API key.

For this reason, it's best practice to keep your API keys away from your code, such as in another file. For example, I made a new Python file called "api_key.py" that contains just one variable `your_client_access_token = "MY API KEY"`, and I can import this variable into my notebook with `import api_key`. 

import api_key

By importing this Python file/module, I get access to the variable `your_client_access_token` without ever explicitly typing my secret API token in this notebook. If I wanted to publish this notebook to GitHub, then I could ignore or leave out the "api_key.py" file that actually contains my Client Access Token.

api_key.your_client_access_token

client_access_token = api_key.your_client_access_token

## Making an API Request

Making an API request looks a lot like typing a specially-formatted URL. But instead of getting a rendered HTML web page in return, you get some data in return.

There are a few different ways that we can query the Genius API, all of which are discussed in the [Genius API documentation](https://docs.genius.com/#songs-h2). The way we're going to cover in this lesson is [the basic search](https://docs.genius.com/#search-h2), which allows you to get a bunch of Genius data about any artist or songs that you search for:

`http://api.genius.com/search?q={search_term}&access_token={client_access_token}`

Sticking with our Missy Elliott theme/obsession, we're going to search for Genius data about Missy Elliott.

First we're going to assign the string "Missy Elliott" to the variable `search_term`. Then we're going to make an f-string URL that contains the variables `search_term` and `client_access_token`.

search_term = "Missy Elliott"

genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"

This URL is basically all we need to make a Genius API request. Want proof? Run the cell below and print this URL, then copy and paste it into a new tab in your web browser.

print(genius_search_url)

It doesn't look pretty, but that's a bunch of Genius data about Missy Elliott!

We can programmatically do the same thing by again using the Python library `requests` with this URL. Instead of getting the `.text` of the response, as we did before, we're going to use `.json()`.

[JSON](https://www.w3schools.com/whatis/whatis_json.asp) is a data format that is commonly used by APIs. JSON data can be nested and contains key/value pairs, much like a Python dictionary.

import requests

response = requests.get(genius_search_url)
json_data = response.json()

The JSON data that we get from our Missy Elliott API query looks something like this:

json_data

We can index this data (again, like a Python dictionary) and look at the first "hit" about Missy Elliott from Genius.com.

json_data['response']['hits'][0]

We can tell that this data describes the song "Work It" and contains other information about the song, such as its number of Genius annotations, its number of web page views, and links to images of its album cover.

## Looping Through JSON Data

### Get Song Titles

for song in json_data['response']['hits']:
    print(song['result']['full_title'])

### Get Song Tiles and Page View Counts

for song in json_data['response']['hits']:
    print(song['result']['full_title'], song['result']['stats']['pageviews'])

### Transform Song Titles and Page View Counts into a DataFrame

We can loop through this data, append it into a list, and then transform that list into a Pandas dataframe by calling `pd.DataFrame()`

import pandas as pd

missy_songs = []
for song in json_data['response']['hits']:
    missy_songs.append([song['result']['full_title'], song['result']['stats']['pageviews']])
    
#Make a Pandas dataframe from a list
missy_df = pd.DataFrame(missy_songs)
missy_df.columns = ['song_title', 'page_views']
missy_df

## Transform Song Titles, Page View Counts, & Album Covers into a DataFrame

Just for fun, we can do the same thing but also add links to images of Missy Elliott's album art—and we can actually display those images, too!

To display images in a Pandas dataframe, you need to run `from IPython.core.display import HTML` and make the function `get_image_html()`. We're going to take the image URLs and make them into HTML objects.

from IPython.core.display import HTML

def get_image_html(link):
    image_html = f"<img src='{link}' width='100'>"
    return image_html

missy_songs = []
for song in json_data['response']['hits']:
    missy_songs.append([song['result']['full_title'], song['result']['stats']['pageviews'], song['result']['song_art_image_url']])
    
missy_df = pd.DataFrame(missy_songs)
missy_df.columns = ['song_title', 'page_views','album_cover_url']

#Use the function get_image_html()
missy_df['album_cover'] = missy_df['album_cover_url'].apply(get_image_html)
missy_df

If we call `HTML()` on our dataframe and add the method `.to_html(escape=False)` to the dataframe, then it should display the dataframe with viewable images.

HTML(missy_df[['album_cover', 'page_views', 'song_title']].to_html(escape=False))

## Your Turn! 

Replace "Phoebe Bridgers" with any artist/musician of your choosing and run the following cells.

search_term = "Phoebe Bridgers"

genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"

response = requests.get(genius_search_url)
json_data = response.json()

songs = []
for song in json_data['response']['hits']:
    songs.append((song['result']['full_title'], song['result']['stats']['pageviews'], song['result']['song_art_image_url']))
    
artist_df = pd.DataFrame(songs)
artist_df.columns = ['song_title', 'page_views', 'album_cover_url']

artist_df['album_cover'] = artist_df['album_cover_url'].apply(get_image_html)
HTML(artist_df[['album_cover', 'page_views', 'song_title']].to_html(escape=False))