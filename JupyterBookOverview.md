# Quick Jupyter Book Overview and Directory Structure

The Python package [`jupyter-book`](https://jupyterbook.org/start/build.html) processes the Jupyter notebook files from this repository and outputs them as the publication-quality HTML files that generate the [corresponding website](https://melaniewalsh.github.io/Intro-Cultural-Analytics/).

The HTML files are currently hidden in this branch of the GitHub repository, but you can find them in the [gh-pages branch](https://github.com/melaniewalsh/Intro-Cultural-Analytics/tree/gh-pages).

Below I will briefly explain the structure of this repository and some important Jupyter Book features.

-  `/book` contains all the materials that generate the Jupyter Book
- `/binder` contains materials that set up the virtual [Binder](https://mybinder.org/) environment for running Jupyter notebooks in the cloud 

### Configuration file

The configuration file [`/book/_config.yml`](https://github.com/melaniewalsh/Intro-Cultural-Analytics/blob/master/book/_config.yml) is where I establish key features of the book, such as its title, logo, and whether you can open the Jupyter notebook files in the cloud.
 
### Table of Contents file

The table of contents file `/book/_toc.yml` establishes the table of contents structure on the left-hand side of the web page.

To include a Markdown or Jupyter notebook file in the table of contents, you include the flag `- file:` followed by the file path *without* the file extension, as shown below: 
```
- file: welcome

- part: How To
  chapters:
  - file: How-To-Interact-With-This-Book
    title: Interact With This Book

- part: The Course
  chapters:
  - file: course-schedule
    title: Course Schedule

  - file: syllabus
    title: Course Syllabus
  
- part: The Book
  chapters:
  - file: Command-Line/The-Command-Line

  - file: Python/Python
    sections:
      - file: Python/Installation
      - file: Python/How-to-Use-Jupyter-Notebooks
```

If you want the title in the table of contents to be different from the title in the notebook, you can also specify a different `title` below the `- file:` flag. Finally, you can include section headers within the table of contents by using the `- part` flag or designate nested chapters by including `chapters:`.

### Notebooks

The Jupyter notebook files can be found in directories named for chapters, e.g., `/book/Python`

### Data

Data can be can be found in `/book/data`

### Texts

Data can be can be found in `/book/texts`

### Custom CSS

Custom CSS styling can be found in [`/book/_static/custom.css`](https://github.com/melaniewalsh/Intro-Cultural-Analytics/blob/master/book/_static/custom.css) (it's a bit messy at the moment, sorry)


## How to Build and Publish Jupyter Book with GitHub Pages

- Run `jupyter-book build book` or `jb build book`, where "book" is the directory with your Jupyter notebook files

A fully-rendered HTML version of the book will be built in `/book/_build/html/`. You can push these HTML files to a GitHub pages website by pushing them to the `gh-pages` branch of a GitHub repository.
 
One easy way to push to the `gh-pages` branch is to [install `gh-import`](https://jupyterbook.org/publish/gh-pages.html#push-your-book-to-a-branch-hosted-by-github-pages).

- Then run `ghp-import -n -p -f book/_build/html`


## Learn More About Jupyter Book

You can learn more about Jupyter Book by exploring the documentation: https://jupyterbook.org/intro.html

