# Pandas — Merge Datasets

In this lesson, we're going to demonstrate how to merge two datasets with Pandas. We're going to walk through a real-world example of how I merged two different datasets published by *The Pudding* to create the CSV file that we used in the previous lesson.

---

## Dataset
### *The Pudding*'s Film Dialogue Data

When Hannah Andersen and Matt Daniels [published](https://github.com/matthewfdaniels/scripts/) the data behind their [*Pudding* essay](https://pudding.cool/2017/03/film-dialogue/) about film dialogue, they published this data as a few different CSV files. But I wanted to combine them into a single CSV file.

___

**Import Pandas**

To use the Pandas library, we first need to `import` it.

import pandas as pd

The above `import` statement not only imports the Pandas library but also gives it an alias or nickname — `pd`. This alias will save us from having to type out the entire words `pandas` each time we need to use it. Many Python libraries have commonly used aliases like `pd`.

**Set Display Settings**

By default, Pandas will display 60 rows and 20 columns. I often change [Pandas' default display settings](https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html) to show more rows or columns.

pd.options.display.max_rows = 100

**Read in CSV File**

To read in a CSV file, we will use the function `pd.read_csv()` and insert the name of our desired file path. 

Hannah Andersen and Matt Daniels published one CSV file called "meta_data7.csv" that contains, among things, the title of each movie, the year of its release, and its box office gross.

metadata = pd.read_csv('../data/Pudding/meta_data7.csv', delimiter=',', encoding='utf-8')

metadata

We're going to drop the column "lines_data", which contains information about when during the film each character speaks.

metadata = metadata.drop(columns='lines_data')

They published another CSV file called "character_list5.csv" that contains, among other things, the name, gender, and age of each character as well as the number of words the character speaks.

characters = pd.read_csv('../data/Pudding/character_list5.csv', delimiter=',',encoding='utf-8')

characters

As you can see, the characters DataFrame doesn't include the actual title of the movie in which the character appears or the movie's release year or box office gross. And the metadata datafram doesn't contain any information about the characters. We want that info all in one place. So how can we combine all of this data together?

## Merge Datasets

If you look closely, there's one column that both datasets share in common: "script_id". If two datasets share at least one column in common, we can merge them together based on this column.

We can use the [`pd.merge()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html) and type in the name of the first dataframe, the name of the second dataframe, and the shared column to be merged on.

pd.merge(characters, metadata, on='script_id')

Now we have a combined DataFrame with character and film information.

merged_movie_character = pd.merge(characters, metadata, on='script_id')

## Calculate Dialogue Proportions

We're going to add one more column to this dataset before the next lesson. We're going to calculate the proportion of words spoken in each film by each character. To do so, we're going to `.groupby()` the movie's title and calculate the sum total number of words spoken in each movie. 

merged_movie_character.groupby('title')[['words']].sum()

If we use the `.transform()`, we can turn this groupby into a single column of data.

merged_movie_character.groupby(['title'])[['words']].transform(sum)

total_movie_words = merged_movie_character.groupby(['title'])[['words']].transform(sum)

Then we're going to divide the total number of words spoken by each character by the total number of words spoken in each film.

total_character_words = merged_movie_character[['words']]

total_character_words / total_movie_words

dialogue_proportion = total_character_words / total_movie_words

Then we're going to add it as a new column.

merged_movie_character['proportion_of_dialogue'] = dialogue_proportion

merged_movie_character

## Write to CSV File

Finally, we're going to output this merged and more comprehensive dataset to a CSV file by using the `.to_csv()` method. We set the `index` parameter to `False` to remove the index column (the numbers in the left-most column).

merged_movie_character.to_csv('../data/Pudding/Merged-Pudding-Film-Dialogue.csv', encoding='utf-8', index=False)