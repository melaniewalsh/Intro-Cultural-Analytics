# Introduction to Cultural Analytics & Python
Designed by [Melanie Walsh](https://melaniewalsh.org/) // Powered by [Jupyter Book](https://jupyterbook.org/)

This repository hosts the code for the online textbook, *Introduction to Cultural Analytics & Python*, which offers an introduction to the programming language Python that is specifically designed for people interested in the humanities and social sciences.

The book demonstrates how Python can be used to study cultural materials such as song lyrics, short stories, newspaper articles, tweets, Reddit posts, and film screenplays. It also introduces computational methods such as web scraping, APIs, topic modeling, Named Entity Recognition (NER), network analysis, and mapping.

These materials were originally created to support "Introduction to Cultural Analytics: Data, Computation & Culture," an undergraduate course taught at Cornell University and the University of Washington.

# Jupyter Book Overview and Repository Structure

The Python package [`jupyter-book`](https://jupyterbook.org/intro.html#install-jupyter-book) processes the Jupyter notebook files from this repository and outputs them as the publication-quality HTML files that generate the [corresponding website](https://melaniewalsh.github.io/Intro-Cultural-Analytics/).

The HTML files are currently hidden in this branch of the GitHub repository, but you can find them in the [gh-pages branch](https://github.com/melaniewalsh/Intro-Cultural-Analytics/tree/gh-pages).

Below I will briefly explain the structure of this repository and some important Jupyter Book features.

-  [`/book`](https://github.com/melaniewalsh/Intro-Cultural-Analytics/tree/master/book) contains all the materials that generate the Jupyter Book
- [`/binder`](https://github.com/melaniewalsh/Intro-Cultural-Analytics/tree/master/binder) contains materials that set up the virtual [Binder](https://mybinder.org/) environment for running Jupyter notebooks in the cloud 

### Configuration file

The configuration file [`/book/_config.yml`](https://github.com/melaniewalsh/Intro-Cultural-Analytics/blob/master/book/_config.yml) is where I establish key features of the book, such as the title, logo, and whether users can open the Jupyter notebook files in the cloud.
 
### Table of Contents file

The table of contents file [`/book/_toc.yml`](https://github.com/melaniewalsh/Intro-Cultural-Analytics/blob/master/book/_toc.yml) establishes the table of contents structure on the left-hand side of the web page.

### Data

Data can be can be found in [`/book/data`](https://github.com/melaniewalsh/Intro-Cultural-Analytics/tree/master/book/data)

### Texts

Texts can be can be found in [`/book/texts`](https://github.com/melaniewalsh/Intro-Cultural-Analytics/tree/master/book/texts)

### Custom CSS

Custom CSS styling can be found in [`/book/_static/custom.css`](https://github.com/melaniewalsh/Intro-Cultural-Analytics/blob/master/book/_static/custom.css) (it's a bit messy at the moment, sorry)

# Learn More About Jupyter Book

You can learn more about Jupyter Book by exploring the documentation: https://jupyterbook.org/intro.html

# Acknowledgments
This course was inspired by a range of excellent course materials, including those by [Lauren Klein](https://github.com/laurenfklein/emory-qtm340), [David Mimno](https://mimno.infosci.cornell.edu/info3350/), and [Allison Parrish](https://github.com/aparrish/rwet). The section "Working with Languages Beyond English" was co-authored with [Quinn Dombrowski](http://www.quinndombrowski.com/).

# License

This book is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

# Support This Project

I'm proud to make this book freely available, but if you find it useful, and if you'd like to support its continued development and maintenance, you can [buy me a coffee ☕](https://www.buymeacoffee.com/melaniewalsh).