# Topic Modeling — CSV Files

In these lessons, we're learning about a text analysis method called *topic modeling*. This method will help us identify the main topics or discourses within a collection of texts a single text that has been separated into smaller text chunks.

---

## Dataset

### Am I the Asshole?

```{epigraph}
AITA for lying about my biggest fear on a quiz show and subsequently winning a car and making other contestants lose?

-- Reddit user iwonacar, [r/AmItheAsshole](https://www.reddit.com/r/AmItheAsshole/comments/dmfsum/aita_for_lying_about_my_biggest_fear_on_a_quiz/)
```

In this particular lesson, we're going to use [Little MALLET Wrapper](https://github.com/maria-antoniak/little-mallet-wrapper), a Python wrapper for [MALLET](http://mallet.cs.umass.edu/topics.php), to topic model a CSV file with 2,932 Reddit posts from the subreddit [r/AmITheAsshole](https://www.reddit.com/r/AmItheAsshole/) that have at least an upvote score of 2,000. This is an online forum where people share their personal conflicts and ask the community to judge who's the a**hole in the story. This data was collected with PSAW, a wrapper for the Pushshift API.

___

```{attention}
If you're working in this Jupyter notebook on your own computer, you'll need to have both the Java Development Kit and MALLET pre-installed. For set up instructions, please see [the previous lesson](http://melaniewalsh.github.io/Intro-Cultural-Analytics/Text-Analysis/Topic-Modeling-Set-Up.html).

*If you're working in this Jupyter notebook in the cloud via Binder, then the Java Development Kit and Mallet will already be installed. You're good to go!
```

## Set MALLET Path

Since Little MALLET Wrapper is a Python package built around MALLET, we first need to tell it where the bigger, Java-based MALLET lives.

We're going to make a variable called `path_to_mallet` and assign it the file path of our MALLET program. We need to point it, specifically, to the "mallet" file inside the "bin" folder inside the "mallet-2.0.8" folder. 

path_to_mallet = 'mallet-2.0.8/bin/mallet'

If MALLET is located in another directory, then set your `path_to_mallet` to that file path.

## Install Packages

#!pip install little_mallet_wrapper
#!pip install seaborn

## Import Packages

Now let's `import` the `little_mallet_wrapper` and the data viz library `seaborn`.

import little_mallet_wrapper
import seaborn
import glob
from pathlib import Path
import pandas as pd
import random
pd.options.display.max_colwidth = 100

We're also going to import [`glob`](https://docs.python.org/3/library/glob.html) and [`pathlib`](https://docs.python.org/3/library/pathlib.html#basic-use) for working with files and the file system.

## Get Training Data From CSV File

Before we topic model the Reddit posts, we need to process the posts and prepare them for analysis. The steps below demonstrate how to process texts if they come from a CSV file.

```{note}
We're calling these text files our *training data*, because we're *training* our topic model with these texts. The topic model will be learning and extracting topics based on these texts.
```

reddit_df = pd.read_csv("../data/top-reddit-aita-posts.csv")

reddit_df.head()

reddit_df['selftext'] = reddit_df['selftext'].astype(str)

### Process Reddit Posts

`little_mallet_wrapper.process_string(text, numbers='remove')`

Next we're going to process our texts with the function `little_mallet_wrapper.process_string()`. This function will take every individual post, transform all the text to lowercase as well as remove stopwords, punctuation, and numbers, and then add the processed text to our master list `training_data`.

training_data = [little_mallet_wrapper.process_string(text, numbers='remove') for text in reddit_df['selftext']]

original_texts = [text for text in reddit_df['selftext']]

### Process Reddit Post Titles

We're also going to extract the file name for each Reddit post.

reddit_titles = [title for title in reddit_df['title']]

### Get Dataset Statistics

We can get training data summary statisitcs by using the funciton `little_mallet_wrapper.print_dataset_stats()`.

little_mallet_wrapper.print_dataset_stats(training_data)

## Training the Topic Model

`little_mallet_wrapper.train_topic_model(path_to_mallet,
                      path_to_formatted_training_data,
                      path_to_model,
                      path_to_topic_keys,
                      path_to_topic_distributions,
                      num_topics)`

We're going to train our topic model with the `little_mallet_wrapper.train_topic_model()` function. As you can see above, however, this function requires 6 different arguments and file paths to run properly:

- `path_to_mallet`
- `path_to_formatted_training_data`
- `path_to_model`
- `path_to_topic_keys`
- `path_to_topic_distributions`
- `num_topics`

So we have to set a few things up first.

## Set Number of Topics

We need to make a variable `num_topics` and assign it the number of topics we want returned.

num_topics = 15

## Set Training Data

We already made a variable called `training_data`, which includes all of our processed Reddit post texts, so we can just set it equal to itself.

training_data = training_data

## Set Other MALLET File Paths

Then we're going to set a file path where we want all our MALLET topic modeling data to be dumped. I'm going to output everything onto my Desktop inside a folder called "topic-model-output" and a subfolder specific to the Reddit posts called "Reddit."

All the other necessary variables below `output_directory_path` will be automatically created inside this directory.

#Change to your desired output directory
output_directory_path = 'topic-model-output/reddit'

#No need to change anything below here
Path(f"{output_directory_path}").mkdir(parents=True, exist_ok=True)

path_to_training_data           = f"{output_directory_path}/training.txt"
path_to_formatted_training_data = f"{output_directory_path}/mallet.training"
path_to_model                   = f"{output_directory_path}/mallet.model.{str(num_topics)}"
path_to_topic_keys              = f"{output_directory_path}/mallet.topic_keys.{str(num_topics)}"
path_to_topic_distributions     = f"{output_directory_path}/mallet.topic_distributions.{str(num_topics)}"

## Import Data

We're going to import the data with `little_mallet_wrapper.import_data()`.

little_mallet_wrapper.import_data(path_to_mallet,
                path_to_training_data,
                path_to_formatted_training_data,
                training_data)

## Train Topic Model

Then we're going to train our topic model with `little_mallet_wrapper.train_topic_model()`. The topic model should take about 1-1.5 minutes to train and complete. 

little_mallet_wrapper.train_topic_model(path_to_mallet,
                      path_to_formatted_training_data,
                      path_to_model,
                      path_to_topic_keys,
                      path_to_topic_distributions,
                      num_topics)

## Display Topics and Top Words

To examine the 15 topics that the topic model extracted from the Reddit posts, run the cell below. This code uses the `little_mallet_wrapper.load_topic_keys()` function to read and process the MALLET topic model output from your computer, specifically the file "mallet.topic_keys.15".

topics = little_mallet_wrapper.load_topic_keys(path_to_topic_keys)

for topic_number, topic in enumerate(topics):
    print(f"✨Topic {topic_number}✨\n\n{topic}\n")

## Load Topic Distributions

MALLET also calculates the likely mixture of these topics for every single Reddit post in the corpus. This mixture is really a probability distribution, that is, the probability that each topic exists in the document. We can use these probability distributions to examine which of the above topics are strongly associated with which specific posts.

To get the topic distributions, we're going to use the `little_mallet_wrapper.load_topic_distributions()` function, which will read and process the MALLET topic model output, specifically the file "mallet.topic_distributions.15". 

topic_distributions = little_mallet_wrapper.load_topic_distributions(path_to_topic_distributions)

topic_distributions[0]

It's a bit easier to understand if we pair these probabilities with the topics themselves. As you can see below, Topic 6 "family wedding party want birthday would" has a relatively high probability of existing in the Reddit post "AITA for not attending holiday gatherings?" `.124` while Topic 14 "dog cats dog house would take" has a relatively low probability `.006`.

reddit_post_to_check = "AITA for lying about my biggest fear on a quiz show and subsequently winning a car and making other contestants lose?"

reddit_post_number = reddit_titles.index(reddit_post_to_check)

print(f"Topic Distributions for {reddit_titles[reddit_post_number]}\n")
for topic_number, (topic, topic_distribution) in enumerate(zip(topics, topic_distributions[reddit_post_number])):
    print(f"✨Topic {topic_number} {topic[:6]} ✨\nProbability: {round(topic_distribution, 3)}\n")

## Explore Heatmap of Topics and Texts

We can visualize and compare these topic probability distributions with a heatmap by using the `little_mallet_wrapper.plot_categories_by_topics_heatmap()` function.

We have everything we need for the heatmap except for our list of `target_labels`, the sample of texts that we'd like to visualize and compare with the heatmap. Below we make our list of desired target labels.

target_labels = random.sample(reddit_titles, 7)

little_mallet_wrapper.plot_categories_by_topics_heatmap(reddit_titles,
                                      topic_distributions,
                                      topics, 
                                      #output_directory_path + '/categories_by_topics.pdf',
                                      target_labels=target_labels,
                                      dim= (15, 8)
                                     )

## Display Top Titles Per Topic

We can also display the Reddit posts and titles that have the highest probability for every topic with the `little_mallet_wrapper.get_top_docs()` function.

training_data_reddit_titles = dict(zip(training_data, reddit_titles))
training_data_original_text = dict(zip(training_data, original_texts))

We'll make our own function `display_top_titles_per_topic()` that will display the top Reddit post titles for every topic. This function accepts a given `topic_number` as well as a desired `number_of_documents` to display.

def display_top_titles_per_topic(topic_number=0, number_of_documents=5):
    
    print(f"✨Topic {topic_number}✨\n\n{topics[topic_number]}\n")

    for probability, document in little_mallet_wrapper.get_top_docs(training_data, topic_distributions, topic_number, n=number_of_documents):
        print(round(probability, 4), training_data_reddit_titles[document] + "\n")
    return

**Topic 0**

To display the top 5 Reddit post titles with the highest probability of containing Topic 0, we will run:

display_top_titles_per_topic(topic_number=0, number_of_documents=5)

**Topic 9**

To display the top 5 Reddit post titles with the highest probability of containing Topic 9, we will run:

display_top_titles_per_topic(topic_number=9, number_of_documents=5)

**Topic 8**

To display the top 7 Reddit posts with the highest probability of containing Topic 8, we will run:

display_top_titles_per_topic(topic_number=8, number_of_documents=7)

## Display Topic Words in Context of Original Text

Often it's useful to actually look at the document that has ranked highly for a given topic and puzzle out why it ranks so highly.

To display the original Reddit post texts that rank highly for a given topic, with the relevant topic words **bolded** for emphasis, we are going to make the function `display_bolded_topic_words_in_context()`.

In the cell below, we're importing two special Jupyter notebook display modules, which will allow us to make the relevant topic words **bolded**, as well as the regular expressions library `re`, which will allow us to find and replace the correct words.

from IPython.display import Markdown, display
import re

def display_bolded_topic_words_in_context(topic_number=3, number_of_documents=3, custom_words=None):

    for probability, document in little_mallet_wrapper.get_top_docs(training_data, topic_distributions, topic_number, n=number_of_documents):
        
        print(f"✨Topic {topic_number}✨\n\n{topics[topic_number]}\n")
        
        probability = f"✨✨✨\n\n**{probability}**"
        reddit_title = f"**{training_data_reddit_titles[document]}**"
        original_text = training_data_original_text[document]
        topic_words = topics[topic_number]
        topic_words = custom_words if custom_words != None else topic_words

        for word in topic_words:
            if word in original_text:
                original_text = re.sub(f"\\b{word}\\b", f"**{word}**", original_text)

        display(Markdown(probability)), display(Markdown(reddit_title)), display(Markdown(original_text))
    return

**Topic 3**

To display the top 3 original Reddit posts with the highest probability of containing Topic 0 and with relevant topic words bolded, we will run:

display_bolded_topic_words_in_context(topic_number=3, number_of_documents=3)

**Topic 8**

To display the top 3 original Reddit posts with the highest probability of containing Topic 8 and with relevant topic words bolded, we will run:

display_bolded_topic_words_in_context(topic_number=14, number_of_documents=5)