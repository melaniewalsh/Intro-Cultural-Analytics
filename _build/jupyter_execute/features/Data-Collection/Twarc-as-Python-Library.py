# Twarc as Python Library

Though I recommend collecting tweets from the command line, you can also use twarc as a Python library and run it in a Jupyter notebook. To import twarc, run `from twarc import Twarc` (as in the cell below). We're also going to import a library called JSON to help us output a JSON file.

from twarc import Twarc
import json

## Configure Twarc

To use Twarc as a Python library, you'll once again need to configure twarc with your [API keys](https://developer.twitter.com/en/apps) (\*sigh\*). Copy and paste them into the quotation marks below.

consumer_key= ""
consumer_secret = ""
access_token = ""
access_token_secret= ""

Quick tip! If you've already set up your Twitter API keys with `twarc configure`, you can find your API keys by running `open ~/.twarc` (Mac/Chrome OS) from the command line or using the code below (Mac/Chrome OS/Windows):

 Mac/Chrome OS

!open ~/.twarc

 Mac/Chrome OS <img src=https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Windows_logo_-_2012_derivative.svg/1024px-Windows_logo_-_2012_derivative.svg.png width=20 align='center-left' > Windows 

import os
config_filename = os.path.join(os.path.expanduser("~"), ".twarc")
print(open(config_filename).read())

These commands will open/print the ".twarc" document that hosts your API keys, and you can simply copy and paste the correct information into the variables in the cell above, then run the cell below.

twarc = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

## Make Live Tweet Collection Function

Below I've written a Python function called `collect_live_tweets()` that uses `twarc.filter()`. This function accepts a search query, the number of tweets that you want to collect, and a filename with a .jsonl extension. This function will output your Twitter data to a file with this filename.

def collect_live_tweets(search_query, number_of_desired_tweets, filename):    
    
    twarc = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

    tweets = []
    with open(filename, 'w', encoding='utf-8') as outfile:
        for tweet in twarc.filter(search_query):
            if len(tweets) < number_of_desired_tweets:
                tweets.append(tweet)
                json.dump(tweet, outfile)
                outfile.write('\n')
            else:
                break
    return

## Run Live Tweet Collection Function

collect_live_tweets("coronavirus", 100, "coronavirus_filter.jsonl")

Below I've written a Python function called `collect_past_tweets()` that uses `twarc.search()`. This function accepts a search query, the maximum number of tweets that you want to collect, and a filename with a .jsonl extension. This function will output your Twitter data to a file with this filename. 

## Make Past Tweet Collection Function

def collect_past_tweets(search_query, number_of_max_tweets, filename):    
    
    twarc = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

    tweets = []
    with open(filename, 'w', encoding='utf-8') as outfile:
        for tweet in twarc.search(search_query):
            if len(tweets) < number_of_max_tweets:
                tweets.append(tweet)
                json.dump(tweet, outfile)
                outfile.write('\n')
            else:
                break
    return

## Run Past Tweet Collection Function

collect_past_tweets("coronavirus", 1000, "coronavirus_search.jsonl")

collect_past_tweets("\"not with a bang but with a\"", 1000, "bang.jsonl")

collect_past_tweets("touch my face min_retweets:10", 2000, "face.jsonl")

  