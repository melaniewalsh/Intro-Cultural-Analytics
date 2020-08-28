sections:
  - file: features/Homework/HW-1-Command-Line
  - file: features/Homework/HW-1-5-Installation
  - file: features/Homework/HW-2-Variables-Data-Types
  - file: features/Homework/HW-3-Conditionals-Comparisons
  - file: features/Homework/HW-3-Lists-Loops
  - file: features/Homework/HW-4-Pandas
  - file: features/Homework/HW-5-Functions-Pandas
  - file: features/Homework/HW-6-Twitter-Setup
  - file: features/Homework/HW-7-Twitter-Data
  - file: features/Homework/HW-8-TF-IDF
  - file: features/Homework/HW-9-Topic-Modeling
  - file: features/Homework/HW-10-NER
  - file: features/Homework/Save-Txt


- file: features/Final-Project/Final-Project
title: Final Project


*directory-name* = name of your desired directory path (e.g. `/Users/melaniewalsh/coding-project`) <br>
*filename* = name of your desired file (e.g. `Frankenstein.txt`)

| Mac OS Terminal        | Explanation                                                                                                | Windows Command Prompt       | Windows PowerShell        |
|:---------------------------:|:-----------------------------------------------------------------------------------------------------------:|:---------------------------:|:--------------------------------:|
| `cd` *filepath*  | **c**hange **d**irectory, aka move into a different folder                                                | `cd` *filepath* | `cd` *filepath*      |
| `ls`                      | **l**i**s**t the files and folders in your current **dir**ectory                                          | `dir`                     | `ls` / `dir` / `Get-ChildItem` |
| `pwd`                     | show **p**ath of **w**orking **d**irectory, aka the folder that you're in right now                       | `cd`                      | `pwd` / `cd`                   |
| `touch` *filename*                   | make a new file                                                                                           |                           | `ni` *filename*                           |
| `mkdir` *directory-name*                   | **m**a**k**e a new **dir**ectory, aka a folder                                                            | `mkdir` *directory-name*                   | `mkdir` *directory-name*                        |
| `rm` *filename*                      | **r**e**m**ove, aka delete, a file or directory                                                           | `del` *filename*                     | `rm` *filename* / `del` *filename*                   |
| `cp` *original-filename* *copied-filename*                      | **c**o**p**y a file or directory                                                                          | `copy` *original-filename* *copied-filename*                    | `cp` / `copy`                  |
| `mv` *original-filename* *new-filename*                      | **m**o**v**e or rename a file or directory                                                                | `move` *original-filename* *new-filename* / `ren` *original-filename* *new-filename*            | `move` *original-filename* *new-filename* / `ren` *original-filename* *new-filename*                 |
| `cat` *filename*                     | show all the contents of a file                                                                           |                           | `cat` *filename* / `type` *filename*                 |
| `less` *filename*                    | show snippet of a file that allows you to scroll through the entire thing                                 | `more` *filename*                      | `more` *filename*                           |
| `head *filename*`                    | show the first 10 lines of a file (change number of lines by adding `-*a number*` flag, e.g. `head -100`) |                           |    `gc` *filename* `-head 10`                           |
| `tail` *filename*                    | show the last 10 lines of a file (change number of lines by adding `-*a number*` flag, e.g. `tail -100`)  |                           | `gc` *filename* `-tail 10`                                  |
| `wc -w -l` *filename*                      | show how many **w**ords or lines in a file                            |                           | `gc` *filename* \| `Measure-Object -Word –Line`                               |
| `man` *command*                     | show the **man**ual, aka the documentation that tells you what a particular command does                  | `help`                    | `help`                         |
| `echo`                    | print text to the command line                                                                            | `echo`                    | `echo`                         |
| `grep` *filename* or *directoryname*                    |                                                                                                           | `findstr` *filename*                 | `findstr` *filename*                      |
| `curl -O` *url* or `wget` *url*                    |  **get**, a file from the **w**eb                                                            |                           | `wget` *url* `-OutFile` *new-filename*         |


```{margin} Note on Terms
:class: terminology
Technically speaking, **command line**, **shell**, **bash**, and **terminal** all mean slightly different things. The Digital Humanities Research Institute provides [a helpful primer on the distinctions](https://github.com/DHRI-Curriculum/glossary/blob/master/sections/command-line.md#glossary).

Also GUI is pronounced ***gooey***, like [St. Louis gooey butter cake](https://en.wikipedia.org/wiki/Gooey_butter_cake).
```