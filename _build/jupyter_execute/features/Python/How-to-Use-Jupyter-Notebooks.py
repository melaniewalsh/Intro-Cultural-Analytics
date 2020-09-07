# How to Use Jupyter Notebooks

A [Jupyter notebook](https://jupyter.readthedocs.io/en/latest/install.html#jupyter-notebook-interface) is a document that can combine live programming code, text, images, and pretty displays of data all in the same place. This combination makes Jupyter notebooks clutch for exploring data as well as for learning and teaching.

A Jupyter notebook has a special .ipynb file extension and can only be opened if you have the application JupyterLab or Jupyter Notebook installed and running. However, one of the cool things about Jupyter Book, which powers this online textbook, is that you can open a Jupyter notebook in the cloud (via Binder or Google Colab) without any prior installation or configuration.

## Some of Jupyter's Nice Features

This document is a Jupyter notebook! Let's quickly demonstrate some of the features that make Jupyter notebooks useful.

### Display Data

We can display and explore data in a readable and aesthetically-pleasing way.

For example, here's a snippet of a CSV file with some data about films and character dialogue, compiled by [The Pudding](https://github.com/matthewfdaniels/scripts/). We'll be working with this data in a later lesson.

import pandas as pd
movie_data = pd.read_csv('../data/Pudding/Pudding-Film-Dialogue-Clean.csv')
movie_data.tail(5)

### Make Data Visualizations 

We can create visualizations based on the above data in the very same document.

Here's a plot of *The Pudding* films by year of their release.

movie_data.groupby('release_year')['title'].count().plot(title='Films By Year')

### Combine Code, Text, Images, and Links

We can combine code, text, images, and links.

For example, here's some data about *Beauty and the Beast*.

movie_data[movie_data['title'] =='Beauty and the Beast']

Now here's an image of *Beauty and the Beast* characters.

![Beauty and the Beast characters image](https://upload.wikimedia.org/wikipedia/en/b/b6/BeautyBeastCharacters.jpg)

See the section Code vs Markdown Cells below for more information about how to include text, images, and links in a Jupyter notebook.

## How to Launch JupyterLab

To open a Jupyter notebook file (.ipynb), you need to have a Jupyter application both installed *and* running. This is confusing for many beginners. If you have Jupyter installed, it seems like you should just be able to click a Jupyter notebook to open it, but you need to launch the application program Jupyter Notebook or JupyterLab first.

```{margin}
To be clear, I use Jupyter *n*otebook with a lowercase *n* to refer to the document (.ipynb file) and Jupyter *N*otebook with a capital *N* to refer to the application program.
```

In this class, we're using JupyterLab as our primary Jupyter application program. JupyterLab and Jupyter Notebook are very similar programs, but JupyterLab is newer and has a bigger and better user interface as well as other improved features. 

### Anaconda Navigator

There are two main ways you can launch JupyterLab. First, you can launch JupyterLab from Anaconda Navigator. You can find Anaconda Navigator in your Applications folder or by searching your computer.

<img src="../images/installation/navigator-app.png" width=80%  >

Once Anaconda Navigator opens, you can launch JupyterLab by clicking "Launch" under the JupyterLab icon.

<img src="https://docs.anaconda.com/_images/nav-defaults.png" widht=80% >

### Command Line

Second, you can launch Jupyter lab from the command line — but only if it is added to your PATH.

%jupyter lab

```{attention}
JupyterLab will open from whatever location you launch from on the command line
```

### Wait Why is JupyterLab Opening in My Web Browser?

JupyterLab opens in a web browser. But JupyterLab is not connected to the internet. It is simply running on a local server on your own personal computer.

## How to Shut Down JupyterLab

To shut down JupyterLab, you can go to File -> Shut Down.

You can also shut down JupyterLab from the command line by pressing `Control` + `C`.

## How to Make a New Jupyter Notebook

To make a new Jupyter notebook, select the Python 3 icon under "Notebook."

<img src="../images/make-new-Jupyter.png" width=80% >

## How to Create and Run a Cell

* You can create a new cell by clicking the plus `+` sign in the toolbar or by pressing `Option` + `Return` (Mac) / `Alt` `Return` (Windows)

* You can run the cell by cliking the play button ▶️ on the toolbar above or by typing `Shift` + `Return`.

from IPython.display import IFrame
IFrame("../videos/create-and-run-cell.mp4", width='100%', height='400px')

## Code vs Markdown Cells

Jupyter notebooks are made up of *cells*, which can either contain code or [Markdown](https://www.markdownguide.org/getting-started/) text. Markdown is a simple "language" that allows you to include formatting instructions directly in the text — bold, italics, headers, links, imgages, code, and more. Markdown is used all over the internet, including on [Reddit](https://www.reddit.com/wiki/markdown#wiki_quick_reference) and on [GitHub](https://guides.github.com/features/mastering-markdown/).

````{list-table}
:header-rows: 1

* - Markdown Syntax
  - Markdown Results
* - ```
    To make text *italics*
    ```
  - To make text *italics*
* - ```
    To make text **bold***
    ```
  -  To make text **bold**
* - ```
    To make text a [link](https://melaniewalsh.org/)
    ```
  - To make text a [link](https://melaniewalsh.org/) 
* - ```
     To make text `code`
     ```
  - To make text `code` 
````

* You can change the cell from "Code" to "Markdown" by clicking the drop down in the toolbar.

* For more on what you can do with Markdown, see Adam Pritchard's [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

## How to Save Your Notebook

If you want to save your notebook, press `Command ⌘` + `S` (Mac) / `Windows Key` + `S` (Windows).