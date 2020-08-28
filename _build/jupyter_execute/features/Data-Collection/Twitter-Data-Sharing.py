# Twitter Data Sharing

In this lesson, we're going to learn how to share Twitter data and access Twitter data that has been shared by others with the Python/command line tool [twarc](https://github.com/DocNow/twarc). This tool was developed by a project called [Documenting the Now](https://www.docnow.io/). The DocNow team develops tools and ethical frameworks for social media research.

This lesson presumes that you've already installed and configured twarc, which was covered in [a previous lesson](https://melaniewalsh.github.io/Intro-Cultural-Analytics/Collecting-Cultural-Data/Twitter-Data-Collection.html#Install-and-Configure-Twarc)).

## Tweet IDs

Twitter discourages developers and researchers from sharing full Twitter data openly on the web. They instead encourage developers and researchers to share *tweet IDs*:

> [If you provide Twitter Content to third parties, including downloadable datasets or via an API, you may only distribute **Tweet IDs**, Direct Message IDs, and/or User IDs.](https://developer.twitter.com/en/developer-terms/policy#4-e)

Tweet IDs are unique identifiers assigned to every tweet. They look like a random string of numbers: 1189206626135355397. Each tweet ID can be used to download the full data associated with that tweet (if the tweet still exists). This is a process called "hydration."

<img src="https://cdn.pixabay.com/photo/2013/07/12/19/24/sapling-154734_960_720.png" width=100% >

**Hydration: a young tweet ID sprouts into a full tweet (to be read in David Attenborough's voice)**

There are actually two reasons that you might want to dehydrate tweets and/or hydrate tweet IDs: first, to responsibly share Twitter data with others and/or access Twitter data shared by others; second, to get more information about the Twitter data that you yourself collected.

If you collected tweets in real time, for example, you collected those tweets immediately after they were published, which means that they will not contain any retweet or favorite count information. Nobody's had time to retweet them yet! So if you'd like to retroactively get retweet and favorite count information about your tweets, then you would want to dehydrate and rehydrate them.

## Dehydrate Tweets

`twarc dehydrate tweets.jsonl > tweet_ids.txt`

To transform your Twitter data into a list of tweet IDs (so that you can share your data openly on the web), you can run the twarc command `twarc dehydrate` with the name of your JSONL file followed by the output operator `>` and the desired name of your tweet ID text file.

> tweet ID —> tweet = hydration <br>
> tweet ID <— tweet = dehydration

Let's dehydrate the Twitter data that we collected about "Infinite Jest" from only verified Twitter accounts.

!twarc dehydrate infinite_jest_verified_tweets.jsonl > infinite_jest_verified_tweets.txt

If we `open()` and `.read()` the tweet IDs file that we just created, it looks something like this:

tweet_ids = open("infinite_jest_verified_tweets.txt", encoding="utf-8").read()

print(tweet_ids)

## Hydrate Tweets

`twarc hydrate tweet_ids.txt > tweets.jsonl`

To transform a list of tweet IDs into full Twitter data, you can run the twarc command `twarc hydrate` with the name of your tweet IDs text file followed by the output operator `>` and the desired name of your JSONL file.

> tweet ID —> tweet = hydration <br>
> tweet ID <— tweet = dehydration

Now let's re-hydrate the Twitter data that we collected a few weeks ago based on the tweet IDs that we just dehydrated.

!twarc hydrate infinite_jest_verified_tweets.txt > infinite_jest_verified_tweets_REHYDRATED.jsonl

tweet_json = open("infinite_jest_verified_tweets_REHYDRATED.jsonl", encoding="utf-8").read()

print(tweet_json)

## Deleted Tweets & The Right To Be Forgotten

What happens if someone decides to delete their tweet between the time when the tweet is first collected and the time when the tweet is "hydrated"? The deleted tweet will **not** be hydrated. The deleted tweet is no longer be accessible.

To see how many tweets might be gone from our dataset, let's look at how many tweets are included in our rehydrated tweet file vs our original tweet file.

 Mac/Chrome OS

!wc -l infinite_jest_verified_tweets.jsonl

!wc -l infinite_jest_verified_tweets_REHYDRATED.jsonl

<img src=https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Windows_logo_-_2012_derivative.svg/1024px-Windows_logo_-_2012_derivative.svg.png width=20 align='left' > Windows 

!find /v /c "" infinite_jest_verified_tweets.jsonl

!find /v /c "" infinite_jest_verified_tweets_REHYDRATED.jsonl

As you can see, our rehydrated tweet file is missing 10 tweets. Those tweets have either been deleted, been made private, or been suspended.

## Separate Out Deleted Tweets (From Tweet IDs)

`python twarc/utils/tweet_compliance.py tweet_ids.txt > hydrated_tweets.json 2> deleted_tweet_ids.txt`

If you're working from someone else's tweet IDs, you can hydrate these tweet IDs and filter out the tweet IDs that have been deleted/made private/suspended by using the twarc utility `twarc/utils/tweet_compliance.py`, followed by the output operator `>`, a JSONL file name for your hydrated tweets, the number `2`, another output operator `>` and a file name for the deleted tweet IDs.

!python twarc/utils/tweet_compliance.py infinite_jest_verified_tweets.txt > hydrated_tweets.json 2> infinite_jest_verified_tweets_deleted_tweets.txt

 Mac/Chrome OS

!wc -l infinite_jest_verified_tweets_deleted_tweets.txt

<img src=https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Windows_logo_-_2012_derivative.svg/1024px-Windows_logo_-_2012_derivative.svg.png width=20 align='left' > Windows 

!find /v /c "" infinite_jest_verified_tweets_deleted_tweets.txt

## Find Current Status of Tweets (From Tweet JSONL File)

`python twarc/utils/deletes.py tweest.jsonl > current_status_of_tweets.txt`

If you want to find out the current status of tweets that you've already collected, you can use the twarc utility `twarc/utils/deletes.py` followed by the output operator `>` then the file name for your text file.

!python twarc/utils/deletes.py infinite_jest_verified_tweets.jsonl > current_status_of_tweets.txt

tweet_current_status = open("current_status_of_tweets.txt", encoding="utf-8").read()

print(tweet_current_status)

## Update/Enhance Twitter Data with Current Status of Tweets

`python twarc/utils/deletes.py --enhance tweets.jsonl > tweets_with_current_status.jsonl`

!python twarc/utils/deletes.py --enhance infinite_jest_verified_tweets.jsonl > infinite_jest_verified_tweets_CURRENT_STATUS.jsonl

## Where to Find Tweet IDs

- DocNow Catalog: https://catalog.docnow.io/

- George Washington University Tweet IDs: https://dataverse.harvard.edu/dataverse/gwu-libraries