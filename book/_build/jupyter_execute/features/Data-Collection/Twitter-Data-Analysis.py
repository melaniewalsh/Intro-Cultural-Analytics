# Twitter Data Analysis

In this lesson, we're going to learn how to analyze and explore Twitter data with Pandas and the Python/command line tool [twarc](https://github.com/DocNow/twarc). This tool was developed by a project called [Documenting the Now](https://www.docnow.io/). The DocNow team develops tools and ethical frameworks for social media research.

This lesson presumes that you've already installed and configured twarc and collected some Twitter data (covered in the previous lesson).

## Twarc

**Search**

Search for tweets that mentioned "Infinite Jest" from the last 7-14 days, only from verified accounts

`twarc search "Infinite Jest filter:verified" > infinite_jest_verified_tweets.jsonl`

**JSON to CSV**

Transform .jsonl to .csv file

!python twarc/utils/json2csv.py --extra-field rt_text retweeted_status.full_text infinite_jest_verified_tweets.jsonl > infinite_jest_verified_tweets.csv

## Read in Tweet CSV files with Pandas

**Import Pandas**

import pandas as pd

**Set Pandas Display Options**

Set Pandas display options so columns are wider and more columns are visible

pd.set_option('max_colwidth', 5000)
pd.set_option('max_columns', 40)
pd.set_option('max_rows', 100)

**Read in CSV file**

infinite_jest_df = pd.read_csv('infinite_jest_verified_tweets.csv')

**Check Columns**

Check what Twitter metadata exists in this CSV file

infinite_jest_df.columns

As you can see above, there is a *lot* of metadata that comes with every tweet!

**Check Shape**

Check the size of dataframe (number of rows = number of tweets)

infinite_jest_df.shape

**Preview DataFrame**

infinite_jest_df.head()

  

  

## Filter Twitter Data

infinite_jest_df[['created_at', 'tweet_type', 'media', 'text', 'rt_text','retweet_count',  'urls', 'user_name', 'user_location', 'hashtags', ]].head(100)

infinite_jest_df = infinite_jest_df[['created_at', 'tweet_type', 'media', 'tweet_url', 'text', 'rt_text','retweet_count',  'urls', 'user_name', 'user_location', 'hashtags', ]].head(100)


## Display Links and Images in Twitter Data

To display links and images in our Twitter dataframe, run the cells below. We're converting the image URL into an HTML image tag and then displaying our dataframe as an HTML object.

from IPython.core.display import HTML

def get_image_html(link):
    if link != "No Image":
        image_html = f"<a href= '{link}'>'<img src='{link}' width='500px'></a>                            "
    else:
        image_html = "No Image"
    return image_html

infinite_jest_df['media'] = infinite_jest_df['media'].fillna("No Image")
infinite_jest_df['media']= infinite_jest_df['media'].apply(get_image_html)

HTML(infinite_jest_df.sort_values(by='media').to_html(render_links=True, escape=False))

Filter to just text, images, and retweet count

HTML(infinite_jest_df[['media', 'text', 'retweet_count']].sort_values(by='media').to_html(render_links=True, escape=False))

## Sort By Top Retweets

infinite_jest_df.sort_values(by='retweet_count', ascending=False)

## Identify Top Hashtags

`twarc/utils/tags.py tweets.jsonl`

 > <img src=https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Windows_logo_-_2012_derivative.svg/1024px-Windows_logo_-_2012_derivative.svg.png width=20 align='left' > Heads up Windows users! Remember that twarc utilities may not work on your computer by default. If you get a UnicodeEncodeError, it's because Windows computers do not use Unicode (UTF-8) by default. However, you can make UTF-8 your default by following [these instructions](https://scholarslab.github.io/learn-twarc/08-win-region-settings) and restarting your comptuer. Then twarc utilities should work.

!python twarc/utils/tags.py infinite_jest_verified_tweets.jsonl

## Create a Word Cloud

`twarc/utils/wordcloud.py tweets.jsonl`

!python twarc/utils/wordcloud.py infinite_jest_verified_tweets.jsonl > infinite_jest_verified_tweets.html

[infinite_jest_verified_tweets.html](infinite_jest_verified_tweets.html)

%%html
<iframe src="infinite_jest_verified_tweets.html" width=800, height=800></iframe>

## Count Emojis

`python twarc/utils/emojis.py tweets.jsonl --number 10`

**Install emoji package**

!pip install emoji

!python twarc/utils/emojis.py infinite_jest_verified_tweets.jsonl --number 10

## Your Turn!

Now choose your own Twitter search term or query.

**Collect Tweets From Last 7 Days**

!twarc search "your search query" > your_search.jsonl 

**Count How Many Tweets You Collected**

 Mac/Chrome OS

!wc -l your_search.jsonl

<img src=https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Windows_logo_-_2012_derivative.svg/1024px-Windows_logo_-_2012_derivative.svg.png width=20 align='left' > Windows 

!find /v /c "" your_search.jsonl

**Convert Your JSON data to CSV data**

!python twarc/utils/json2csv.py --extra-field rt_text retweeted_status.full_text  your_search.jsonl > your_search.csv

**Read in CSV file**

import pandas as pd

your_df = pd.read_csv('your_search.csv')

**Add Metadata**

Filter your dataframe and add at least one new metadata column that we haven't explored yet.

your_df.columns

When you run the cell below, right-click to "Enable Scrolling for Outputs" and scroll through to see what the new metadata category looks like. Discuss this category with your group and how you might use it for a Twitter analysis.

your_df[['created_at', 'tweet_type', '#YOUR NEW METADATA HERE','media', 'tweet_url', 'text', 'rt_text','retweet_count',  'urls', 'user_name', 'user_location', 'hashtags', ]].head(100)

Now save your filtered dataframe as `filtered_df`

#Your Code Here

**Explore Data with Links and Images**

from IPython.core.display import HTML

def get_image_html(link):
    if link != "No Image":
        image_html = f"<a href= '{link}'>'<img src='{link}' width='500px'></a>                            "
    else:
        image_html = "No Image"
    return image_html

filtered_df['media'] = filtered_df['media'].fillna("No Image")
filtered_df['media']= filtered_df['media'].apply(get_image_html)

HTML(filtered_df.to_html(render_links=True, escape=False))

**Sort Your Twitter Data by Top Retweets**

#Your code here

What is the most retweeted tweet in your dataset?

**#**Your Answer Here

**Count Most Frequent Emojis**

!python twarc/utils/emojis.py your_search.jsonl --number 10