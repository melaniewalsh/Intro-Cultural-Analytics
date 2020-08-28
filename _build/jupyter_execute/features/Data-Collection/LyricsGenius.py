# Song Lyrics Collection

In this lesson, we're going to use a Python package called [LyricsGenius](https://github.com/johnwmillr/LyricsGenius) to collect song lyrics about any artist and album.

## API Wrappers
An API wrapper is a package that makes an API easier to use and/or extends the API's functionality. A data scientist named John Miller wrote a Python package called [LyricsGenius,](https://github.com/johnwmillr/LyricsGenius) which makes working with the Genius API easier and adds functionality not offered by the Genius API.

Remember when I said that companies typically don't offer access to their most lucrative data? Well, the Genius API doesn't offer you a way to get access to song lyrics. To solve this problem, LyricsGenius combines the Genius API with the web scraping library BeautifulSoup to get and save song lyrics.

## Install the Package

To install LyricsGenius (and get the most updated version from GitHub), run:

!pip install git+https://github.com/johnwmillr/LyricsGenius.git

Copy and paste your Genius "Client Access Token" into the quotation marks below, and run the cell to save your variable :

client_access_token = "INSERT YOUR CLIENT ACCESS TOKEN IN THESE QUOTATION MARKS"

Import and initialize LyricsGenius

import lyricsgenius
LyricsGenius = lyricsgenius.Genius(client_access_token)

## Get Songs and Lyrics By a Specific Artist

To get the top songs and song lyrics from a specific artist you can use the method `.search_artist()`:

artist = LyricsGenius.search_artist("Missy Elliott", max_songs=6)

To access the song titles, you can run `artist.songs`:

artist.songs

Inside each of those songs, LyricsGenius has already saved the song lyrics. You can access these lyrics by looping through `artist.songs` and pulling out `song.lyrics`:

for song in artist.songs:
    print(song.lyrics)

## Get Specific Song and Lyrics By a Specific Artist

To get the song lyrics from a specific artist, you can use the method `.search_song()`

song = LyricsGenius.search_song("Missy Elliott", "Work It")

song.lyrics

## Save Lyrics to .txt File

song.save_lyrics(extension='txt')

## Get Songs and Lyrics For a Specific Album

As you can see, LyricsGenius is an extremely useful Python package! But one thing that we can't do with LyricsGenius is get all the song lyrics for a particular album.

So we're going to use the web scraping functions that we wrote in the last lesson to get all the song titles for a specific album, then use LyricsGenius to get the lyrics for each of those songs, and then save them all as text files in a directory.

**Import necessary Python libraries**

from bs4 import BeautifulSoup
import re
import lyricsgenius
import requests
from pathlib import Path

**Make RegEx Function To Clean Up Songs**

def clean_up(song_title):

    if "Ft" in song_title:
        before_ft_pattern = re.compile(".*(?=\(Ft)")
        song_title_before_ft = before_ft_pattern.search(song_title).group(0)
        clean_song_title = song_title_before_ft.strip()
        clean_song_title = clean_song_title.replace("/", "-")
    
    else:
        song_title_no_lyrics = song_title.replace("Lyrics", "")
        clean_song_title = song_title_no_lyrics.strip()
        clean_song_title = clean_song_title.replace("/", "-")
    
    return clean_song_title

**Make Function To Scrape Song Titles For Album**

def get_all_songs_from_album(artist, album_name):
    
    artist = artist.replace(" ", "-")
    album_name = album_name.replace(" ", "-")
    
    response = requests.get(f"https://genius.com/albums/{artist}/{album_name}")
    html_string = response.text
    document = BeautifulSoup(html_string, "html.parser")
    song_title_tags = document.find_all("h3", attrs={"class": "chart_row-content-title"})
    song_titles = [song_title.text for song_title in song_title_tags]
    
    clean_songs = []
    for song_title in song_titles:
        clean_song = clean_up(song_title)
        clean_songs.append(clean_song)
        
    return clean_songs

**Make Function To Download Lyrics For All Songs in Album**

def download_album_lyrics(artist, album_name): 
    
    # Set up LyricsGenius with your Genius API client access token
    #client_access_token = Your-Client-Access-Token
    LyricsGenius = lyricsgenius.Genius(client_access_token)
    LyricsGenius.remove_section_headers = True
    
    # With the function that we previously created, go to Genius.com and get all song titles for a particular artist's album
    clean_songs = get_all_songs_from_album(artist, album_name)
    
    for song in clean_songs:
        
        #For each song in the list, search for that song with LyricsGenius
        song_object = LyricsGenius.search_song(song, artist)
        
        #If the song is not empty
        if song_object != None:
            
            #Do some cleaning and prep for the filename of the song
            artist_title = artist.replace(" ", "-")
            album_title = album_name.replace(" ", "-")
            song_title = song.replace("/", "-")
            song_title = song.replace(" ", "-")
            
            #Establish the filename for each song inside a directory that begins with the artist's name and album title
            custom_filename=f"{artist_title}_{album_title}/{song_title}"
            
            #A line of code that we need to create a directory
             #os.makedirs(os.path.dirname(filename), exist_ok=True)
            Path(f"{artist_title}_{album_title}").mkdir(parents=True, exist_ok=True)
            
            #Save the lyrics for the song as a text file
            song_object.save_lyrics(filename=custom_filename, extension='txt', sanitize=False)
        
        #If the song doesn't contain lyrics
        else:
            print('No lyrics')

**Call the function**

download_album_lyrics("Missy Elliott", "Under Construction")