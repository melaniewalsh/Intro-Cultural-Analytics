# Pandas Basics — Part 3

In this lesson, we're going to introduce more fundamentals of [Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/overview.html), a powerful Python library for working with tabular data like CSV files.

We will review skills learned from the last two lessons and introduce how to:

- Check for duplicate data
- Clean and transform data
- Manipulate string data
- Apply functions
- Reset index
- Bonus! Create an interactive data viz

___

## Dataset
### *The Pudding*'s Film Dialogue Data

```{epigraph}
Lately, Hollywood has been taking so much shit for rampant sexism and racism. The prevailing theme: white men dominate movie roles.
But it’s all rhetoric and no data, which gets us nowhere in terms of having an informed discussion. How many movies are actually about men? What changes by genre, era, or box-office revenue? What circumstances generate more diversity?

-- Hannah Anderson and Matt Daniels, ["Film Dialogue from 2,000 screenplays, Broken Down by Gender and Age"](https://pudding.cool/2017/03/film-dialogue/)
```

The dataset that we're working with in this lesson is taken from Hannah Andersen and Matt Daniels's *Pudding* essay, ["Film Dialogue from 2,000 screenplays, Broken Down by Gender and Age"](https://pudding.cool/2017/03/film-dialogue/). The dataset provides information about 2,000 films from 1925 to 2015, including characters’ names, genders, ages, how many words each character spoke in each film, the release year of each film, and how much money the film grossed. They included character gender information because they wanted to contribute data to a broader conversation about how "white men dominate movie roles."

Yet transforming complex social constructs like gender into quantifiable data is tricky and historically fraught. They claim, in fact, that one of the [most frequently asked questions](https://medium.com/@matthew_daniels/faq-for-the-film-dialogue-by-gender-project-40078209f751) about the piece is about gender: “Wait, but let’s talk about gender. How do you know the monster in Monsters Inc. is a boy!" The short answer is that they don't. To determine character gender, they used actors' IMDB information, which they acknowledge is an imperfect approach: "Sometimes, women voice male characters. Bart Simpson, for example, is voiced by a woman. We’re aware that this means some of the data is wrong, AND we’re still fine with the methodology and approach."

As we work with this data, we want to be critical and cognizant of 

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

film_df = pd.read_csv('../data/Pudding/Pudding-Film-Dialogue-Salty.csv', delimiter=",", encoding='utf-8')

When reading in the CSV file, we also specified the `encoding` and `delimiter`. The `delimiter` parameter specifies the character that separates or "delimits" the columns in our dataset. For CSV files, the delimiter will most often be a comma. (CSV is short for *Comma Separated Values*.) Sometimes, however, the delimiter of a CSV file might be a tab (`/t`) or, more rarely, another character.

**Display Data**

We can display a DataFrame in a Jupyter notebook simply by running a cell with the variable name of the DataFrame.

```{margin} NaN
`NaN` is the Pandas value for any missing data.  

See ["Working with missing data"](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html?highlight=nan) for more information
```

film_df

There are a few important things to note about the DataFrame displayed here:

* Index
    * The bolded ascending numbers in the very left-hand column of the DataFrame is called the Pandas *Index*. You can select rows based on the Index.
    * By default, the Index is a sequence of numbers starting with zero. However, you can change the Index to something else, such as one of the columns in your dataset.

* Truncation
    * The DataFrame is truncated, signaled by the ellipses in the middle `...` of every column.
    * The DataFrame is truncated because we set our default display settings to 100 rows. Anything more than 100 rows will be truncated. To display all the rows, we would need to alter Pandas' default display settings yet again.

* Rows x Columns
    * Pandas reports how many rows and columns are in this dataset at the bottom of the output (23,052 x 10 columns).

**Display First *n* Rows**

To look at the first *n* rows in a DataFrame, we can use a method called `.head()`.

film_df.head(10)

**Display Random Sample**

To look at a random sample of rows, we can use the `.sample()` method.

film_df.sample(10)

**Examine Data**

**Shape**

To explicitly check for how many rows vs columns make up a dataset, we can use the `.shape` method.

film_df.shape

There are 23,052 rows and 10 columns.

**Data Types**

Just like Python has different data types, Pandas has different data types, too. These data types are automatically assigned to columns when we read in a CSV file. We can check these Pandas data types with the [`.dtypes` method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html).



| **Pandas Data Type** |  **Explanation**                                                                                   |
|:-------------:|:---------------------------------------------------------------------------------------------------:|
| `object`         | string                                                                               |
| `float64`         | float                                               |
| `int64`       | integer                                                        |
| `datetime64`       |  date time              

film_df.dtypes

It's important to always check the data types in your DataFrame. For example, sometimes numeric values will accidentally be interpreted as a string object. To perform calculations on this data, you would need to first convert that column from a string to an integer.

**Columns**

We can also check the column names of the DataFrame with [`.columns`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html)

film_df.columns

**Summary Statistics**

film_df.describe(include='all')

Do you notice any outliers, anomalies, or potential problems here?

The maximum value in the "age" column is 2013! That seems like an error.

film_df[film_df['age'] == 2013]

Let's drop this row from the dataset by using the `.drop()` method and the Index number of the row.

film_df = film_df.drop(11639)

Now if we look for it again, that row is gone.

film_df[film_df['age'] == 2013]

**Rename Columns**

film_df = film_df.rename(columns={'imdb_character_name': 'character', 'year': 'release_year'})

film_df.head()

**Drop Columns**

film_df = film_df.drop(columns='imdb_id')

**Missing Data**

**.isna() / .notna()**

Pandas has special ways of dealing with missing data. As you may have already noticed, blank rows in a CSV file show up as `NaN` in a Pandas DataFrame.

To filter and count the number of missing/not missing values in a dataset, we can use the special `.isna()` and `.notna()` methods on a DataFrame or Series object. 

The `.isna()` and `.notna()` methods return True/False pairs for each row, which we can use to filter the DataFrame for any rows that have information in a given column. 

film_df[film_df['character'].isna()]

This is important information for the sake of better understanding our dataset. But it's also important because `NaN` values are treated as *floats*, not *strings*. If we tried to manipulate this column as text data, we would get an error. For this reason, we're going to replace or "fill" these `NaN` values with the string "No Character Data" by using the `.fillna()` method.

film_df['character'] = film_df['character'].fillna('No Character Data')

film_df[film_df['character'].isna()]

## Check for Duplicates 

### Duplicates

We can check for duplicate rows by using the `.duplicated()` method and setting the parameter `keep=False`, which will display all the duplicated values in the dataset — rather than just the first duplicated value `keep='first'` or the last duplicated value `keep='last'`.

film_df.duplicated(keep=False)

The output above is reporting whether each row in the dataset is a duplicate. We can use the `.duplicated()` method inside a filter to isolate only the rows in the dataframe that are exact duplicates.

film_df[film_df.duplicated(keep=False)]

We can drop duplicates from the DataFrame with the `.drop_duplicates()` method and choose to keep the first instance of the duplicate or the last instance.

film_df = film_df.drop_duplicates(keep='first')

Now if we check the data for duplicates again, they should be all gone.

film_df[film_df.duplicated(keep=False)]

## Clean and Transform Data

### Pandas `.str` Methods

Remember all the special things that you can do with Python strings aka [string methods](https://melaniewalsh.github.io/Intro-Cultural-Analytics/Python/String-Methods.html)?

Pandas has special [Pandas string methods](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#string-methods), too. Many of them are very similar to Python string methods, except they will transform every single string value in a column, and we have to add `.str` to the method chain.

| **Pandas String Method** | **Explanation**                                                                                   |
|:-------------:|:---------------------------------------------------------------------------------------------------:|
| df['column_name']`.str.lower()`         | makes the string in each row lowercase                                                                                |
| df['column_name']`.str.upper()`         | makes the string in each row uppercase                                                |
| df['column_name']`.str.title()`         | makes the string in each row titlecase                                                |
| df['column_name']`.str.replace('old string', 'new string')`      | replaces `old string` with `new string` for each row |
| df['column_name']`.str.contains('some string')`      | tests whether string in each row contains "some string" |
| df['column_name']`.str.split('delim')`          | returns a list of substrings separated by the given delimiter |
| df['column_name']`.str.join(list)`         | opposite of split(), joins the elements in the given list together using the string                                                                        |
                                                            

For example, to transform every character's name in the "character" column from lowercase to uppercase, we can use `.str.upper()` 

film_df['character'].str.upper()

To transform every character's name in the "character" column to lowercase, we can use `.str.lower()`

film_df['character'].str.lower()

If we want to replace the gender columns's single letter abbreviation for "male" / "female" (sex) with "man" / "woman" (gender identity), we could use the `.str.replace()` method. 

film_df['gender'] = film_df['gender'].str.replace('m', 'man')

film_df['gender'] = film_df['gender'].str.replace('f', 'woman')

film_df.sample(10)

We can use the `.str.contains()` to search for particular words or phrases in a column, such as "Star Wars."

film_df[film_df['title'].str.contains('Star Wars')]

We can use the `.str.contains()` to search for particular words or phrases in a column, such as "Mean Girls."

film_df[film_df['title'].str.contains('Mean Girls')]

## Applying Functions

With the `.apply()` method, we can run a function on every single row in a Pandas column or dataframe.

def make_text_title_case(text):
    title_case_text = text.title()
    return title_case_text

make_text_title_case("betty")

film_df['character'].apply(make_text_title_case)

film_df['character'] = film_df['character'].apply(make_text_title_case)

film_df.sample(10)

**Filter DataFrame**

We can filter the DataFrames for only characters who are men or women.

men_film_df = film_df[film_df['gender'] == 'man']

women_film_df = film_df[film_df['gender'] == 'woman']

**Groupby**

We can use the `.groupby()` function to group all the men characters in each film and sum up their total dialogue.

By adding a Python string slice, we can identify the top 20 films with the greatest proportion of men speaking.

```{margin} Line Breaks
If a line of code gets too long, you can create a line break with a backslash `\`
```

men_film_df.groupby('title')[['proportion_of_dialogue']]\
.sum().sort_values(by='proportion_of_dialogue', ascending=False)[:20]

We can use the `.groupby()` function to group all the women characters in each film and sum up their total dialogue.

By adding a Python string slice, we can identify the top 20 films with the greatest proportion of women speaking.

```{margin} Line Breaks
If a line of code gets too long, you can create a line break with a backslash `\`
```

women_film_df.groupby('title')[['proportion_of_dialogue']]\
.sum().sort_values(by='proportion_of_dialogue', ascending=False)[:20]

## Reset Index

We can transform a Groupby object into a DataFrame with a regular Index by tacking on `.reset_index()`.

```{margin} Line Breaks
If a line of code gets too long, you can create a line break with a backslash `\`
```

women_film_df.groupby('title')[['proportion_of_dialogue']]\
.sum().sort_values(by='proportion_of_dialogue', ascending=False).reset_index()

## Bonus — Interactive Data Visualization

#Set up Bokeh to work in Jupyter notebook
output_notebook()

Here's an interactive data visualization of these Hollywood films by release year and percentage of women dialogue. This data viz was created with the Python library [Bokeh](https://docs.bokeh.org/en/latest/index.html), which we will discuss in some later lessons.

* Scroll to zoom in
* Hover to see more information about each point

To see the code that created this visualization, select "Click to show" below.

#Make groupby into a new DataFrame
dialogue_df = women_film_df.groupby(['title', 'release_year'])[['proportion_of_dialogue']].sum().sort_values(by='proportion_of_dialogue', ascending=False).reset_index()

#Import necessary Bokeh bodules
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.io import output_notebook, show
from bokeh.palettes import RdBu
from bokeh.transform import linear_cmap, jitter

# Set up the source data that will suppply the x,y columns and the film title hover text
source = ColumnDataSource(dialogue_df)

# Set the hover tool tip to the film title, release year, and proportion of dialogue

TOOLTIPS = [("Title", "@title"),
            ("Year", "@release_year"),
           ("Women Dialogue", "@{proportion_of_dialogue}{%0.2f}")]

#Set up Bokeh plot with title, labels, 
bokeh_plot = figure(title="How Much Do Women Speak in Hollywood Films?", x_axis_label = 'Film Release Year',
                    y_axis_label = 'Amount of Dialogue Spoken By Women',x_range = [1930, 2018], y_range = [0, 1.01],
                 tooltips=TOOLTIPS, width=900, height=850, active_scroll='wheel_zoom')

# Create a red to blue color palette
color_mapper = linear_cmap(field_name='proportion_of_dialogue', palette=RdBu[4], low=1.1, high=0)

# Supply inidivudal points values
bokeh_plot.circle(y='proportion_of_dialogue', x=jitter('release_year', width=.2),
         size = 20,
        line_color='black',
        line_alpha=.4,
         source=source,
         color=color_mapper, alpha=.5)

bokeh_plot.title.text_font_size='20pt'

#Make Y axis percentages
bokeh_plot.yaxis.formatter = NumeralTickFormatter(format='0 %')

show(bokeh_plot)

