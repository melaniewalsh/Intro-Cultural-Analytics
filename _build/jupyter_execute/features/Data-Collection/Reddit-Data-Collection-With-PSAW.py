# Reddit Data Collection with PSAW 

## Install PSAW

!pip install psaw

**Import Pandas and Set Display Options**

import pandas as pd
pd.set_option('max_colwidth', 500)
pd.set_option('max_columns', 50)

## Import PushshiftAPI

from psaw import PushshiftAPI

## Initialize PushshiftAPI

api = PushshiftAPI()

## Collect Reddit submissions (with more than a certain upvote score)

**Set up generator to make API request**

api_request_generator = api.search_submissions(subreddit='AmITheAsshole', score = ">2000")

**Grab data for each Reddit submission and make into a DataFrame**

The cell below should take a while to run. It's searching through Reddit's entire history. It's ok if you periodically get errors while it's running.

aita_submissions = pd.DataFrame([submission.d_ for submission in api_request_generator])

**Check shape**

aita_submissions.shape

**Check columns**

aita_submissions.columns

**Transform to datetime**

aita_submissions['date'] = pd.to_datetime(aita_submissions['created_utc'], utc=True, unit='s')

aita_submissions[['author', 'date', 'title', 'selftext', 'url', 'subreddit', 'score', 'num_comments', 'num_crossposts', ]]

## Collect Reddit submissions (with search keyword)

**Set up generator to make API request**

The cell below should only take a second to run

api_request_generator = api.search_submissions(q='Missy Elliott', score = ">2000")

**Grab data for each Reddit submission and make into a DataFrame**

The cell below should take a while to run. It's searching through Reddit's entire history. It's ok if you periodically get errors while it's running.

missy_submissions = pd.DataFrame([submission.d_ for submission in api_request_generator])

missy_submissions['date'] = pd.to_datetime(missy_submissions['created_utc'], utc=True, unit='s')

missy_submissions[['author', 'date', 'title', 'selftext', 'url', 'subreddit', 'score', 'num_comments', 'num_crossposts', ]]

missy_submissions['subreddit'].value_counts()

## Collect Reddit comments (with search keyword)

**Set up generator to make API request**

The cell below should only take a second to run

api_request_generator = api.search_comments(q='Missy Elliott', score = ">2000")

### Grab data for each Reddit comment that mentions query and make into a dataframe

**Grab data for each Reddit comment and make into a DataFrame**

The cell below should take a while to run. It's searching through Reddit's entire history. It's ok if you periodically get errors while it's running.

missy_comments = pd.DataFrame([comment.d_ for comment in api_request_generator])

## Collect Reddit submissions/comments (with multiple search keywords)

To search for multiple phrases —  George Orwell OR J.R.R. Tolkein — use parentheses and the bitwise OR operator

api_request_generator = api.search_comments(q='(George Orwell)|(J. R. R. Tolkien)')

To search for multiple phrases —  Shakespeare AND Beyonce — use parentheses and the bitwise AND operator

api_request_generator = api.search_comments(q='(Shakespeare)&(Beyonce)')

## Collect Reddit submissions/comments (with start and end dates)

import datetime as dt
start_epoch=int(dt.datetime(2020, 1, 1).timestamp())
end_epoch=int(dt.datetime(2020, 1, 10).timestamp())

api_request_generator = api.search_comments(q='(Shakespeare)&(Beyonce)"', after = start_epoch, before=end_epoch)