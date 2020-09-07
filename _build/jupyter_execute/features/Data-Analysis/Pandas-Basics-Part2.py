# Pandas Basics — Part 2

In this lesson, we're going to introduce some more fundamentals of [Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/overview.html), a powerful Python library for working with tabular data like CSV files.

We will review skills learned from the last lesson and introduce how to:

* Broadly examine data
* Work with missing data
* Rename, drop, and add new columns
* Perform mathematical calculations
* Aggregate subsets of data
* Make a simple time series

___

## Dataset
### The Trans-Atlantic Slave Trade Database

```{epigraph}
[D]isplaying data alone could not and did not offer the atonement descendants of slaves
sought or capture the inhumanity of this archive’s formation.

-- Jessica Marie Johnson, <a href="https://read.dukeupress.edu/social-text/article/36/4%20(137)/57/137032/Markup-BodiesBlack-Life-Studies-and-Slavery-Death">“Markup Bodies”</a>
```

The dataset that we're going to be working with in this lesson is taken from [The Trans-Atlantic Slave Trade Database](https://www.slavevoyages.org/voyage/database), part of the [*Slave Voyages* project](https://www.slavevoyages.org/). The larger database includes information about 35,000 slave-trading voyages from 1514-1866. The dataset we're working with here was filtered to include the 20,000 voyages that landed in the Americas. The data was filtered to also include the percentage of enslaved men, women, and children on the voyages.

We're working with this data for a number of reasons. The *Slave Voyages* project is a major data-driven contribution to the history of slavery and to the field of the digital humanities. Before the Trans-Atlantic Slave Trade Database, as DH scholar Jessica Johnson [writes,](https://read.dukeupress.edu/social-text/article-abstract/36/4%20(137)/57/137032/Markup-BodiesBlack-Life-Studies-and-Slavery-Death?redirectedFrom=fulltext) "historians assumed enslaved women and children played a negligible role in the slave trade." But evidence from the Trans-Atlantic Slave Trade Database suggested otherwise. "The existence of the Trans-Atlantic Slave Trade Database immediately reshaped debates about numbers of women and children exported from the continent," Johnson says, "influencing work on women in the slave trade on the African coast, slavery in African societies, and women in the slave trade to the Americas."

Though the Trans-Atlantic Slave Trade Database helped shed new light on the roles of enslaved women and children, Johnson makes clear that it was not computation or data alone that shed this light: 
> [D]isplaying data alone could not and did not offer the atonement descendants of slaves sought or capture the inhumanity of this archive’s formation. Culling the lives of women and children from the data set required approaching the data with intention. It required a methodology attuned to black life and to dismantling the methods used to create the manifests in the first place, then designing and launching an interface responsive to the desire of descendants of slaves for reparation and redress.

In this spirit, we want to think about how responsible data analysis requires more than just data and technical tools like Pandas. It requires approaching data with intention and developing methodologies geared toward justice. This is especially necessary when dealing with data that records and perpetrates violence like the Trans-Atlantic Slave Trade Database.

___

**Import Pandas**

To use the Pandas library, we first need to `import` it.

import pandas as pd

The above `import` statement not only imports the Pandas library but also gives it an alias or nickname — `pd`. This alias will save us from having to type out the entire words `pandas` each time we need to use it. Many Python libraries have commonly used aliases like `pd`.

**Set Display Settings**

By default, Pandas will display 60 rows and 20 columns. I often change [Pandas' default display settings](https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html) to show more rows or columns.

pd.options.display.max_rows = 100

**Read in CSV File**

````{sidebar}
```{tip} 
If you use the `help()` function, you can see the documentation for almost any bit of code. If we run it on `pd.read_csv()`, we can see all the possible parameters that can be used with `pd.read_csv()`.
help(pd.read_csv)
```
````

To read in a CSV file, we will use the function `pd.read_csv()` and insert the name of our desired file path. 

slave_voyages_df = pd.read_csv('../data/Trans-Atlantic-Slave-Trade_Americas.csv', delimiter=",", encoding='utf-8')

This creates a Pandas [DataFrame object](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#DataFrame) — often abbreviated as *df*, e.g., *slave_voyages_df*. A DataFrame looks and acts a lot like a spreadsheet. But it has special powers and functions that we will discuss in the next few lessons.

When reading in the CSV file, we also specified the `encoding` and `delimiter`. The `delimiter` specifies the character that separates or "delimits" the columns in our dataset. For CSV files, the delimiter will most often be a comma. (CSV is short for *Comma Separated Values*.) Sometimes, however, the delimiter of a CSV file might be a tab (`/t`) or, more rarely, another character.

**Display Data**

We can display a DataFrame in a Jupyter notebook simply by running a cell with the variable name of the DataFrame.

```{margin} NaN
`NaN` is the Pandas value for any missing data.  

See ["Working with missing data"](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html?highlight=nan) for more information
```

slave_voyages_df

There are a few important things to note about the DataFrame displayed here:

* Index
    * The bolded ascending numbers in the very left-hand column of the DataFrame is called the Pandas *Index*. You can select rows based on the Index.
    * By default, the Index is a sequence of numbers starting with zero. However, you can change the Index to something else, such as one of the columns in your dataset.

* Truncation
    * The DataFrame is truncated, signaled by the ellipses in the middle `...` of every column.
    * The DataFrame is truncated because we set our default display settings to 100 rows. Anything more than 100 rows will be truncated. To display all the rows, we would need to alter Pandas' default display settings yet again.

* Rows x Columns
    * Pandas reports how many rows and columns are in this dataset at the bottom of the output (20,741 x 14 columns).

**Display First *n* Rows**

To look at the first *n* rows in a DataFrame, we can use a method called `.head()`.

slave_voyages_df.head(10)

## Examine Data

### Shape

To explicitly check for how many rows vs columns make up a dataset, we can use the `.shape` method.

slave_voyages_df.shape

There are 20,741 rows and 14 columns.

### Data Types

Just like Python has different data types, Pandas has different data types, too. These data types are automatically assigned to columns when we read in a CSV file. We can check these Pandas data types with the [`.dtypes` method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html).



| **Pandas Data Type** |  **Explanation**                                                                                   |
|:-------------:|:---------------------------------------------------------------------------------------------------:|
| `object`         | string                                                                               |
| `float64`         | float                                               |
| `int64`       | integer                                                        |
| `datetime64`       |  date time              

slave_voyages_df.dtypes

It's important to always check the data types in your DataFrame. For example, sometimes numeric values will accidentally be interpreted as a string object. To perform calculations on this data, you would need to first convert that column from a string to an integer.

### Columns

We can also check the column names of the DataFrame with [`.columns`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html)

slave_voyages_df.columns

### Summary Statistics

slave_voyages_df.describe(include='all')

## Missing Data

```{epigraph}
The conceit of the archive is that it is the repository of answers, of knowable conclusions, of the data needed to explain or understand the past.

The reality, however, is that the archive is the troubled genesis of our always-failed effort to unravel the effects of the past on the present; rather than verifiable truths, the archive — and its silences — house the very questions that unsettle us.

-- Jennifer Morgan, ["Accounting for 'The Most Excruciating Torment'"](https://read.dukeupress.edu/history-of-the-present/article-abstract/6/2/184/153282/Accounting-for-The-Most-Excruciating-Torment?redirectedFrom=PDF)
```

Responsible data analysis requires understanding missing data. The Trans-Atlantic Slave Trade Database, as historian Jennifer Morgan [writes](https://read.dukeupress.edu/history-of-the-present/article-abstract/6/2/184/153282/Accounting-for-The-Most-Excruciating-Torment?redirectedFrom=PDF), contains innumerable "silences" and "gaps." These silences include the thoughts, feelings, and experiences of the enslaved African people on board the voyages — silences that cannot be found in the database itself.

There are other kinds of silences and gaps that can be detected in the database itself, however. For example, while some of the voyages in the the Trans-Atlantic Slave Trade Database recorded information about how many enslaved women and children were aboard, most did not. Yet focusing on the data that is there and analyzing trends in the missing data can help shed light on the history of gender and enslavement. The fact that most ship captains did not record gender information, Morgan argues, helps tells us about their "priorities": "[W]e can assume that had it been financially significant to have more men than women that data would have been more scrupulously recorded."

### .isna() / .notna()

Pandas has special ways of dealing with missing data. As you may have already noticed, blank rows in a CSV file show up as `NaN` in a Pandas DataFrame.

To filter and count the number of missing/not missing values in a dataset, we can use the special `.isna()` and `.notna()` methods on a DataFrame or Series object.

slave_voyages_df['percent_women'].notna()

The `.isna()` and `.notna()` methods return True/False pairs for each row, which we can use to filter the DataFrame for any rows that have information in a given column. For example, we can filter the DataFrame for only rows that have information about the percentage of enslaved women aboard the voyage.

slave_voyages_df[slave_voyages_df['percent_women'].notna()]

The data is now filtered to only include the 2,894 rows with information about how many women were aboard the voyage.

To explicitly count the number of blank rows, we can use the `.value_counts()` method.

slave_voyages_df['percent_women'].isna().value_counts()

There are 17,874 that do not contain information about the number of enslaved women on the voyage (`isna` = True) and 2,894 rows that do contain this information (`isna` = False).

To quickly transform these numbers into percentages, we can set the `normalize=` parameter to True.

slave_voyages_df['percent_women'].isna().value_counts(normalize=True)

About 14% of rows in this dataset have information about the number of enslaved women on the voyage while 86% do not.

### .count()

Because the `.count()` method always excludes NaN values, we can also count the number of values in each column and divide by the total number of rows in each column (`len()`) to find the percentage of not blank data in every column.

slave_voyages_df.count() / len(slave_voyages_df)

For example, 100% of the rows in the columns "year_of_arrival" contain information, while 2% of the rows in the column "resistance_label" contain information. The "resistance_label" indicates whether there is a record of the enslaved Africans aboard the voyage staging some form of resistance.

### .fillna()

If we wanted, we could fill the `NaN` values in the DataFrame with a different value by using the `.fillna()` method.

slave_voyages_df['percent_women'].fillna('no gender information recorded')

## Rename Columns

We can rename columns with the [`.rename()` method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html) and the `columns=` parameter. For example, we can rename the "flag" column "national_affiliation."

slave_voyages_df.rename(columns={'flag': 'national_affiliation'})

Renaming the "flag" column as above will only momentarily change that column's name, however. If we display our DataFrame, we will see that the column name has *not* changed permamently.

slave_voyages_df.head(1)

To save changes in the DataFrame, we need to reassign the DataFrame to the same variable.

slave_voyages_df = slave_voyages_df.rename(columns={'flag': 'national_affiliation'})

slave_voyages_df.head(1)

## Drop Columns

We can remove a column from the DataFrame with the `.drop()` method and the column name.

slave_voyages_df = slave_voyages_df.drop(columns="sources")

slave_voyages_df.columns

## Add Columns

To add a column, we simply put a new column name in square brackets and set it equal to whatever we want the new column to be.

For example, if we wanted to create new columns for the total women and men aboard each voyage, we could set them equal to the product of the "total_disembarked" column * the "percent_women" / "percent_men" columns.

slave_voyages_df['total_women'] = slave_voyages_df['total_embarked'] * slave_voyages_df['percent_women']

slave_voyages_df['total_men'] = slave_voyages_df['total_embarked'] * slave_voyages_df['percent_men']

If we scroll all the way to the right side of the DataFrame, we can see that these columns have been added.

slave_voyages_df.head(1)

## Sort Columns

We can sort a DataFrame with the `.sort_values()` method, inside of which we include the parameter `by=` and indicate the name of the column we want to sort by (written in quotation marks).

For example, we can sort the DataFrame by the voyages that had the largest proportion of enslaved women aboard.

slave_voyages_df.sort_values(by='percent_women', ascending=False)

By default, Pandas will sort in "ascending" order, from the smallest value to the largest value. If we want to sort the largest values first, we need to include another parameter `ascending=False`.

Because the DataFrame is truncated when it has more than 100 rows, we can use a Python list slice to view the top 30 (or any number less than 100) voyages with enslaved women aboard.

slave_voyages_df.sort_values(by='percent_women', ascending=False)[:30]

If we want to sort a Series object, we don't need to use the `by=` paramter.

slave_voyages_df['total_women'].sort_values(ascending=False)

## Calculate Columns

We can do different calculations on columns with built-in Pandas functions. These calculations will ignore `NaN` values.

| Pandas calculations | Explanation                         |
|----------|-------------------------------------|
| `.count()`    | Number of observations    |
| `.sum()`      | Sum of values                       |
| `.mean()`     | Mean of values                      |
| `.median()`   | Median of values         |
| `.min()`      | Minimum                             |
| `.max()`      | Maximum                             |
| `.mode()`     | Mode                                |
| `.std()`      | Unbiased standard deviation         |



For example, to find the average proprotion of enslaved women aboard the voyages (for voyages that have this information), we can use the `.mean()` method.

slave_voyages_df['percent_women'].mean()

There were on average 27% enslaved women aboard the voyages for voyages that recorded this information.

slave_voyages_df['percent_women'].max()

The highest percentage of women aboard the slave voyages was 100%. We can use this calculation as a filter to identify the voyage(s) with this maximum value.

slave_voyages_df[slave_voyages_df['percent_women'] == slave_voyages_df['percent_women'].max()]

According to the Trans-Atlantic Slave Trade Database, the 1819 voyage of the S José Diligente had 100% enslaved women aboard.

As demonstrated previously, we can also perform calculations with columns themselves.

(slave_voyages_df['total_embarked'] * slave_voyages_df['percent_women']).max()

## Groupby Columns

The Pandas function`.groupby()` allows us to group data and perform calculations on the groups.

For example, Jennifer Morgan writes about how some nations recorded more information about the gender of the enslaved people aboard their voyages than other nations did. To see the breakdown of gender information by nation, we can use a `.groupby()` function.

The first step to using groupby is to type the name of the DataFrame followed by `.groupby()` with the column we'd like to aggregate based on, such as "national_affiliation."

slave_voyages_df.groupby('national_affiliation')

This action will created a [GroupBy object](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html). We can perform calculations on this grouped data, such as counting the number of non-blank values in each column for each nation.

slave_voyages_df.groupby('national_affiliation').count()

```{sidebar} On England's Slave Ship Records
> For example, patterns emerge that suggest that English slave ship captains provided the most data related to the age or sex characteristics of the captives they transported and sold into slavery...The degree to which the practice of recording the sex of the passengers on board accords to national origin raises some interesting questions about the possible correlations between certain notational and national presumptions of accountability.

-Jennifer Morgan, ["Accounting for 'The Most Excruciating Torment'"](https://read.dukeupress.edu/history-of-the-present/article-abstract/6/2/184/153282/Accounting-for-The-Most-Excruciating-Torment?redirectedFrom=PDF)
```

We can also isolate only the "percent_women" column.

slave_voyages_df.groupby('national_affiliation').count()['percent_women']

slave_voyages_df.groupby('national_affiliation')['percent_women'].count().sort_values(ascending=False)

```{margin} Line Breaks
If a line of code gets too long, you can create a line break with a backslash `\`
```

slave_voyages_df.groupby('national_affiliation')['percent_women'].count()\
.sort_values(ascending=False).plot(kind='bar', title='Trans-Atlantic Slave Trade (Americas): \n Slave Voyages with Recorded Gender Information')

## Make Time Series with Groupby

To make a time series, we would typically want to convert our date column into datetime values rather than integers.

slave_voyages_df['year_of_arrival'].dtype

Datetime values allow us to do special things that we can't do with regular integers and floats, such as extract just the year, month, week, day, or second from any date or aggregate based on any of the above.

Since we're only working with year information, however, we can make some simple time series plots just by grouping by the year column and performing calculations on those year groupings, such as calculating the average percentage of enslaved women aboard the voyages over time.

slave_voyages_df.groupby('year_of_arrival')['percent_women'].mean()\
.plot(title="Trans-Atlantic Slave Trade (Americas):\nAverage Percentage of Enslaved Women on Voyages")

We can do the same thing with the total number of women, this time taking the sum for every year.

slave_voyages_df.groupby('year_of_arrival')['total_women'].sum()\
.plot(kind='area', title="Trans-Atlantic Slave Trade (Americas):\nTotal Number of Enslaved Women on Voyages")

We can plot multiple columns at the same time by using two square brackets. For example, we can compare the total number of women and men aboard the voyages.

slave_voyages_df.groupby('year_of_arrival')[['total_women', 'total_men']].sum()\
.plot(kind='area', title="Trans-Atlantic Slave Trade (Americas):\nTotal Number of Enslaved Women and Men on Voyages")

Finally, we can also add in the total number of enslaved people who embarked on the voyages, offering a perspective of how mcuh gender information we have about the voyages compared to the total number of voyages.

slave_voyages_df.groupby('year_of_arrival')[['total_women',  'total_men', 'total_embarked']].sum()\
.plot(kind='area', title='Trans-Atlantic Slave Trade (Americas):\nTotal Number of Enslaved People on Voyages')