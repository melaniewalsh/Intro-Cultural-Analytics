# Twitter Data Collection

In this lesson, we're going to learn how to collect Twitter data with the Python/command line tool [twarc](https://github.com/DocNow/twarc). This tool was developed by a project called [Documenting the Now](https://www.docnow.io/). The DocNow team develops tools and ethical frameworks for social media research.

## Install and Configure Twarc

Because twarc relies on Twitter's API, we need to apply for a Twitter developer account and create a Twitter application before we use it. You can find instructions for the application process and for installing and configuring twarc here: [Twitter Collection Setup](https://melaniewalsh.github.io/Intro-Cultural-Analytics/Collecting-Cultural-Data/Twitter-Collection-Setup.html).

🚨Skip this section if you've already configured twarc!!🚨

You can configure twarc by running `twarc conifgure` on the command line. Or you can type your Twitter handle (without the @ symbol) and [API keys](https://developer.twitter.com/en/apps) into the quotation marks below and run the cell.

#Insert Your Twitter API Info here

twitter_handle = ""
consumer_key= ""
consumer_secret = ""
access_token = ""
access_token_secret= ""

#The Code That Will Configure Twarc
configuration = f"""[{twitter_handle}]
consumer_key={consumer_key}
consumer_secret = {consumer_secret}
access_token = {access_token}
access_token_secret= {access_token_secret}
"""

import os
config_filename = os.path.join(os.path.expanduser("~"), ".twarc")
with open(config_filename, "w") as file_object:
    file_object.write(configuration)

## Twitter API (Free Version)

With the free version of the Twitter API, there are basically two ways to collect your own Twitter data: in real time or ~7 days in the past. To get data any further in the past requires a paid version of the Twitter API. Twarc allows you to collect tweets both in real time and ~7 days in the past.

### Collect Tweets in Real Time

The easiest way to collect tweets with twarc is to use the command line. To collect tweets in real time, you can use the command `twarc filter`, followed by a search query, then the output operator `>` and a filename of your choosing with the ".jsonl" file extension (which outputs your Twitter data to this JSONL file).

`twarc filter "search term" > my_file.jsonl`

For example, to collect tweets in real time that include the word "coronavirus," you would run:

`twarc  filter "coronavirus" > coronavirus_filter.jsonl`

**Starting and Stopping Twarc**

If you run `twarc filter` from your command line, `twarc` will keep running until you explicitly stop the process. You can stop a process on the command line by typing `Ctrl + C`.

As you may recall, we can run command line functions in Jupyter notebooks by putting an exclamation point `!` at the beginning of a cell. For some reason, however, `!twarc filter` and `!twarc search` don't play very well in Jupyter notebooks (or at least they don't play well consistently). Sometimes when you start running them, they won't stop—even when you hit the stop button or try to interrupt the kernel (the equivalent of `Ctrl + C`).

Because of this unpredictability, I recommend that you 1) open your Terminal or PowerShell 2) navigate to the directory that contains this Jupyter notebook 3) and experiment with the twarc code below by copying it and pasting it into your command line, where you can more easily stop the processes.

<img src="../images/twarc-filter-Terminal.png" widht=100% >

Run a live collection of tweets that include the word "coronavirus":

`twarc  filter "coronavirus" > coronavirus_filter.jsonl`

To stop this process:

`Ctrl + C`

Run a live collection of tweets that include the word "Shakespeare":

`twarc filter "Shakespeare" > shakespeare_filter.jsonl`

To stop this process:

`Ctrl + C`

#### Check Number of Tweets Collected

 Mac/Chrome OS

!wc -l coronavirus_filter.jsonl

!wc -l shakespeare_filter.jsonl

<img src=https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Windows_logo_-_2012_derivative.svg/1024px-Windows_logo_-_2012_derivative.svg.png width=20 align='left' > Windows 

!find /v /c "" coronavirus_filter.jsonl

!find /v /c "" shakespeare_filter.jsonl

### Collect Tweets From Past 7 days

To collect tweets from approximately 7 days in the past, you can use the command `twarc search`, followed by a search query, then the output operator `>` and a filename of your choosing with the ".jsonl" file extension (which outputs your Twitter data to this JSONL file).

Run a collection of tweets from the past ~7 days that include the word "coronavirus" for 10 seconds:

`twarc search "coronavirus" > coronavirus_search.jsonl` 

Run a collection of tweets from the last ~7 days that include the word "Shakespeare":

`twarc search "Shakespeare" > shakespeare_search.jsonl`

#### Check Number of Tweets Collected

 Mac/Chrome OS

!wc -l coronavirus_search.jsonl

<img src=https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Windows_logo_-_2012_derivative.svg/1024px-Windows_logo_-_2012_derivative.svg.png width=20 align='left' > Windows 

!find /v /c "" coronavirus_search.jsonl

## Crafting a Good Twitter Query

We made relatively simple queries to Twitter's API in the examples above. But there are more specific and more complex ways to make queries.

To craft a good Twitter search query, it's important to understand and explore these myriad ways. A researcher named Igor Brigadir has compiled a wonderful resource that details many of the Twitter API search operators: https://github.com/igorbrigadir/twitter-advanced-search/blob/master/README.md

### Exact Phrases

`twarc search "\"an exact phrase\""`

You can search for an *exact* phrase in a tweet by including the phrase in escaped `\` quotation marks, as above.

**"Not with a bang but with a..."**

The first phrase that we're going to search for comes from the conclusion of T.S. Eliot's 1925 [poem "The Hollow Men"](https://msu.edu/~jungahre/transmedia/the-hollow-men.html):

>This is the way the world ends<br>
>This is the way the world ends<br>
>This is the way the world ends<br>
>**Not with a bang but with a whimper.**

You've probably heard these lines before, even if you didn't know that they were written by the modernist poet T.S. Eliot. This phrase is a striking example of a bit of literary, poetic language that has gone "viral" in 21st-century American culture, both on and off the internet.

Since there aren't a ton of tweets from the past 7 days that included the phrase "not with a bang but with a", we can run this `twarc search` from our Jupyter notebook. Because there is a small and finite number of tweets to be collected, this search will complete in a relatively short amount of time, and we don't have to worry about it running forever.

!twarc search "\"not with a bang but with a\"" > not_with_bang_tweets.jsonl

### General Phrases

`twarc search "a general phrase"`

**"Touch my face"**

The other phrase we're going to search for comes from public health recommendations about preventing the spread of the coronavirus: that people should avoid touching their faces. Many people are, in light of these recommendations, discovering that it's actually very difficult not to touch your own face.

Now the avoidance of touching one's face has sprouted up as a funny Twitter meme. These various "touch my face" memes serves as an interesting example of how online communities produce comedy and levity even in times of stress and crisis.

%%html
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Realizing basically all I do is touch my face.</p>&mdash; Seth Rogen (@Sethrogen) <a href="https://twitter.com/Sethrogen/status/1234905018475499520?ref_src=twsrc%5Etfw">March 3, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Similarly, there aren't a ton of tweets from the past 7 days that included the phrase "touch my face", so we can also run this `twarc search` from our Jupyter notebook.

!twarc search "touch my face" > touch_my_face_tweets.jsonl 

  

Great! Now we have some Twitter data. But before we dive into analysis, we need to complete one more step. We need to convert this JSON data to CSV data, which will be easier for us to work with. Luckily, there's a twarc "utility" for this very purpose.

### Minimum Retweets

`twarc search "a general phrase min_retweets:1000"`

### Only Verified Accounts

`twarc search "a general phrase min_retweets:1000"`

## Twarc Utilities

There are a number of twarc "utilities" that enable you to manipulate and analyze Twitter data. With these utilities, you can do things such as convert JSON data to CSV data, count up the most frequent emojis used in tweets, make a network visualization of tweets and Twitter users, and more.

These utilities are not available from the `pip install twarc` installation. To access the twarc utilities, you'll need to `git clone` the [twarc GitHub repository](https://github.com/DocNow/twarc) or download it as a zip file.

The twarc repository should already be downloaded in your relevant files, but if you uncomment the line below, you can also clone the repository with this line of code.

#!git clone https://github.com/DocNow/twarc.git

### Use Twarc Utilities

`python twarc/utils/your_desired_util.py tweets.jsonl`

To use a twarc utility, you need to call `python` from the command line and then include the utility's file path (they all should be in the "twarc/utils" subfolder).

Note that if your Jupyter notebook is in exactly the same directory as the "twarc" repository, then you can run the code as above. However, if your Jupyter notebook is somewhere else, you will have to direct it to the correct location of "twarc/utils". For example`python /Users/melaniewalsh/twarc/utils/your_desired_util.py tweets.jsonl`

## Convert JSON to CSV

To convert a JSON file to a CSV file, you can run `python twarc/utils/json2csv.py` followed by the JSONL filename, the output operator `>` and your desired filename for the CSV file.

`python twarc/utils/json2csv.py json_file.jsonl > csv_file.csv`

 > <img src=https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Windows_logo_-_2012_derivative.svg/1024px-Windows_logo_-_2012_derivative.svg.png width=20 align='left' > Heads up Windows users! The twarc utility json2csv.py will probably not work on your computer by default. You'll likely get a UnicodeEncodeError because Windows computers do not use Unicode (UTF-8) by default. However, you can make UTF-8 your default by following [these instructions](https://scholarslab.github.io/learn-twarc/08-win-region-settings) and restarting your comptuer. Then json2csv.py should work.


!python twarc/utils/json2csv.py not_with_bang_tweets.jsonl > not_with_bang_tweets.csv

Make "bang.jsonl" into "bang.csv" (with an extra field added for the full version of the original retweeted text)

!python twarc/utils/json2csv.py --extra-field rt_text retweeted_status.full_text not_with_bang_tweets.jsonl > not_with_bang_tweets.csv

## Twarc as Python Library

Though I recommend collecting tweets from the command line, you can also use twarc as a Python library and run it in a Jupyter notebook. You can find a Jupyter notebook with instructions and guidance about it here: {doc}`Twarc-as-Python-Library`