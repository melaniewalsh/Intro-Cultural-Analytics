# The Command Line

Before we begin learning about the programming language Python, we need to learn about the command line. The command line — also referred to as *the shell*, *bash*, or *terminal* — is the gateway to computational analysis. Think of it like interacting with your computer behind the scenes.

Here are some of the important things that you can do from the command line (and why we're learning about it):

* Run a Python script
* Install software
* Connect to a remote server (i.e., use a different computer from your current computer)
* Do simple tasks faster and more efficiently
* Gain more power and flexibility over your computing experience

<img src="../images/command-line/welcome.png" alt="The command line" class="center">

```{note}
Technically speaking, *command line*, *shell*, *bash*, and *terminal* all mean slightly different things. The Digital Humanities Research Institute provides [a helpful primer on the distinctions](https://github.com/DHRI-Curriculum/glossary/blob/master/sections/command-line.md#glossary).


```

The command line interface is often contrasted with the graphical user interface or GUI (pronounced *gooey*, like [St. Louis gooey butter cake](https://en.wikipedia.org/wiki/Gooey_butter_cake)). This is the way that most people are familiar with navigating their computers. 

To illustrate the difference between the command line and the GUI, consider the following example. I want to make a new folder to organize my notes for this class. So I drag my mouse cursor and click on a button that says "New Folder," which makes a small icon of a folder appear. I title this folder "Intro-CA-Notes." Now I want to delete this folder. So I drag and drop the folder icon into a tiny trash can icon. 

<img src="../images/command-line/GUI-example.gif" alt="Making and deleting a folder with GUI" class="center" >


This is the GUI in action. This is how we interact with our computers *graphically* — with visual icons, movements, and mouse clicks. 

But that's not the only way we can interact with our computers. We can do all of the above from the command line as well. Instead of dragging and dropping little folder icons, we would type in textual commands, such as `mkdir Intro-CA-Notes` (to make a folder/directory) and `rmdir Intro-CA-Notes` (to remove the folder/directory). 

<img src="../images/command-line/CLI-example.gif" alt="Making and deleting a folder with command line" class="center" >

Making a folder from the command line as opposed to dragging and clicking with the mouse won't save us a ton of time. Maybe a couple of seconds at most.

But in the aggregate, with larger tasks, these seconds start to add up. Since we can automate tasks from the command line, we can transform things that would be tedious and time-consuming to do manually — such as resizing 1000 photos or combining a dozen smaller CSV files into one large file — into useful and efficient scripts.

That's just the tip of the iceberg. From the command line, you can also run Python code, install software, connect to a remote server or a [Raspberry Pi](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/), and more. The command line offers you greater power and flexibility over your computing experience.

## Where do I find the command line?

Your command line will differ depending on the operating system (OS) that you're using. Most operating systems fall into two different families: the **Unix-like** family and the **Microsoft Windows** family. The Unix-like family includes Mac OS, Linux, Android, and Chrome.

We're going to focus on the command line interfaces for Mac, Microsoft Windows, and Chromebooks.

###  Mac OS

If you're using a Mac, you will access the command line through an application called "Terminal." You can find Terminal under Applications -> Utilities.

<img src="../images/command-line/Terminal-Applications-Utilities.png" alt="Open Mac Terminal in Applications" class="center">

Alternatively, you can find it by clicking Spotlight Search in the top right corner, typing "Terminal," and double-clicking the application or pressing enter.


from IPython.display import IFrame
IFrame("../videos/Terminal-Keep-In-Dock.mp4", width='100%', height='400px')

You can keep the Terminal application on your dock by right-clicking the application and selecting Options -> Keep in Dock (as shown in the video above).

<img src="../images/command-line/welcome.png" alt="The command line" class="center">

When you open Terminal, you will see the name of your computer and your username followed by a dollar sign `$`. For example, when I go to the command line, I see the prompt `Melanies-MacBook-Pro:~ melaniewalsh$`, as shown above. You type commands after the dollar sign `$`.

```{attention}
If you see a dollar sign `$` in example code in this book or elsewhere, the dollar sign represents where you should start typing your own code. You do not need to include the dollar sign `$` in your own code. It will cause an error. It's a common beginner's mistake to include the dollar sign `$`, especially when consulting examples from the internet.
```

 ### <img src=https://upload.wikimedia.org/wikipedia/commons/3/34/Windows_logo_-_2012_derivative.svg width=20 align=left> Windows OS

The command line for Windows users, called "Command Prompt," is different from the command line interface for Mac users and the wider Unix-like family. The Windows Command Prompt is not as powerful as the Unix shell in certain ways.

```{margin} Google Breakdown
See Google's breakdown of the best [Windows Command-line Tools](https://developers.google.com/web/shows/ttt/series-2/windows-commandline).
```

However, beginning with Windows 7, Microsoft also introduced "PowerShell," which acts like a more flexible and more powerful command line for Windows users. (You can read more about PowerShell in [Microsoft's official documentation](https://docs.microsoft.com/en-us/powershell/?view=powershell-6)).

```{margin} Aliases: An Example
For example, the PowerShell command that lists all the files and folders in a particular directory is `Get-ChildItem`. The traditional Windows Command Prompt command `dir` and the Unix command `ls` also work in PowerShell and perform the same function.
```

We're going to focus on PowerShell, as opposed to Command Prompt, for a number of reasons. One very convenient reason is that PowerShell commands have "aliases." They go by a number of different names, including names that are used by the traditional Windows Command Prompt and by a Mac Terminal.

These aliases will conveniently allow you to learn a little about Unix and Windows commands at the same time. Since we're mostly trying to understand how the command line functions at a broad level, this level of familiarity will suffice for now. In the future, you may want to invest more time in learning the specifics of PowerShell or the Command Prompt.

<img src="https://www.isunshare.com/images/article/windows-10/5-ways-to-open-windows-powershell-in-windows-10/open-windows-powershell-by-search.png" alt="Open Windows PowerShell" class="center" >

To open PowerShell, simply search for it in the Windows search bar, as shown above.

### <img src=https://upload.wikimedia.org/wikipedia/commons/a/a5/Google_Chrome_icon_%28September_2014%29.svg width=20 align=left> Chromebook

To access the command line from a Chromebook, you first need to turn on Linux (Beta). The following instructions are taken from [Google Chromebook Help](https://support.google.com/chromebook/answer/9145439?hl=en).

- At the bottom right, select the time
- Select Settings 
- Under "Linux (Beta)," select Turn On
- Follow the steps on the screen. Setup can take 10 minutes or more
- A terminal window opens. You can run Linux commands, install more tools using the APT package manager, and customize your shell

## Command Line Cheatsheet

| Mac / Chrome / Linux                            | Explanation                                                                                               | Windows PowerShell                                                                   |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| `cd` *filepath*                            | **c**hange **d**irectory, aka move into a different folder                                                | `cd` *filepath*                                                                      |
| `ls`                                       | **l**i**s**t the files and folders in your current **dir**ectory                                          | `ls` / `dir` / `Get-ChildItem`                                                       |
| `pwd`                                      | show **p**ath of **w**orking **d**irectory, aka the folder that you're in right now                       | `pwd` / `cd`                                                                         |
| `touch` *filename*                         | make a new file                                                                                           | `ni` *filename*                                                                      |
| `mkdir` *directory-name*                   | **m**a**k**e a new **dir**ectory, aka a folder                                                            | `mkdir` *directory-name*                                                             |
| `rm` *filename*                            | **r**e**m**ove, aka delete, a file or directory                                                           | `rm` *filename* / `del` *filename*                                                   |
| `cp` *original-filename* *copied-filename* | **c**o**p**y a file or directory                                                                          | `cp` / `copy`                                                                        |
| `mv` *original-filename* *new-filename*    | **m**o**v**e or rename a file or directory                                                                | `move` *original-filename* *new-filename* / `ren` *original-filename* *new-filename* |
| `cat` *filename*                           | show all the contents of a file                                                                           | `cat` *filename* / `type` *filename*                                                 |
| `less` *filename*                          | show snippet of a file that allows you to scroll through the entire thing                                 | `more` *filename*                                                                    |
| `head` *filename*                          | show the first 10 lines of a file (change number of lines by adding `-*a number*` flag, e.g. `head -100`) | `gc` *filename* `-head 10`                                                           |
| `tail` *filename*                          | show the last 10 lines of a file (change number of lines by adding `-*a number*` flag, e.g. `tail -100`)  | `gc` *filename* `-tail 10`                                                           |
| `wc -w -l` *filename*                      | show how many **w**ords or lines in a file                                                                | `gc` *filename* \| `Measure-Object -Word –Line`                                      |
| `man` *command*                            | show the **man**ual, aka the documentation that tells you what a particular command does                  | `help` *command*                                                                               |
| `echo`                                     | print text to the command line                                                                            | `echo`                                                                               |
| `grep` "search term" *filename* or *directory-name*       |      search for lines that include search term in file                                                                                                     | `findstr` "search term" *filename*                                                                 |
| `curl -O` *url* / `wget` *url*            | **get**, a file from the **w**eb                                                                          | `wget` *url* `-OutFile` *new-filename*                                               |


## Basic Navigation and File Structure

```{note}
If you're using these commands outside a Jupyter notebook, you do not need to include the `%` or `!` at the beginning of the line. The `%` and `!` symbols allow access the command line from a Jupyter notebook.
```

*Note: the `%` and `!` symbols at the beginning of the lines below allow us to access the command line from a Jupyter notebook. If you were using these commands outside the Jupyter environemnt, you would not need to include `%` or `!`*

### Display Path of Working Directory

⭐ *You are here!* ⭐ One of the most basic and useful commands is the one that tells you where you are on your computer. Type `pwd` and it will show you the **p**ath of your **w**orking **d**irectory, aka the folder that you're currently in. This might not seem terribly important at the moment, but it 

| Mac / Chrome / Linux                            | Explanation                                                                                               | Windows PowerShell                                                                   |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| `pwd`                                      | show **p**ath of **w**orking **d**irectory, aka the folder that you're in right now                       | `pwd` / `cd`                                                                         |

%pwd

The forward slash `/` before and after each name indicates that the name is a directory. On Windows computers, directories are indicated by backslashes `\`.

This filepath is unique to my personal computer, which you could probably guess because it includes my name. If you open up a command line on your own personal machine and type `pwd`, it should return your personal "home" directory.

### List Files and Folders

If you want to see what's inside the directory that you're currently in, you can run `ls`, which **l**i**s**t all the files and folders.

| Mac / Chrome / Linux                            | Explanation                                                                                               | Windows PowerShell                                                                   |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| `ls`                                       | **l**i**s**t the files and folders in your current **dir**ectory                                          | `ls` / `dir` / `Get-ChildItem`                                                       |


%ls

The output above shows that this directory contains "The-Command-Line.ipynb" (this very Jupyter notebook!) as well as another directory called "very-interesting-folder."

### Change Directory


If we want to find out what's inside that directory, we can move into it by using the **c**hange **d**irectory `cd` command and plugging in the name of the directory

| Mac / Chrome / Linux                            | Explanation                                                                                               | Windows PowerShell                                                                   |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| `cd` *filepath*                            | **c**hange **d**irectory, aka move into a different folder                                                | `cd` *filepath*                                                                      |

%cd very-interesting-folder/

%ls

### Relative Path vs Absolute Path

There are two ways to to tell your computer where you want to go aka your desired *path*.

#### Relative Path

Relative path is a path to a location that's relative to your current location.

We used a relative path when we moved into `very-interesting-folder` because we simply typed:

%cd very-interesting-folder/

Since we were already inside `/Users/melaniewalsh/Intro-Cultural-Analytics/Website-Content/Command-Line/`, that's all the information we needed to get where we wanted to go.

##### Double Dot

A "double dot" `..` allows you to move up to a parent directory one level up.

%cd ..

The double dot is a very convenient way of moving relatively through your file structure.

Most of our text files for this class exist one directory above the Jupyter notebooks, so we're often going to be referencing them with a relative filepath that begins with two periods `../`

#### Absolute Path 

Absolute path is a path to a location from a bird's eye view of your computer.

If we wanted to move inside `very-interesting-folder` from a completely different place on our computers, we could use an absolute path:


%cd ~/Website-Content/Command-Line/very-interesting-folder

##### Home Folder Tilde ~

The tilde symbol (`~`) is an alias for the home folder. If you type the tilde symbol and then tab, it should autocomplete the path for your home folder.

## Working with Files and Texts

There's a lot of basic text analysis that you can do just from the command line.

### Download a text file from the web

| Mac / Chrome / Linux                            | Explanation                                                                                               | Windows PowerShell                                                                   |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| `curl -O` *url* / `wget` *url*            | **get**, a file from the **w**eb                                                                          | `wget` *url* `-OutFile` *new-filename*                                               |


You can download a text file from the web by using the command `curl` or `wget` with the appropriate web address. Let's see if we can download Charlotte Perkins Gilman's short story "The Yellow Wallpaper."

We're going to search for the story through [Project Gutenberg](https://www.gutenberg.org/ebooks/search/), an amazing resource that hosts tens of thousands of free texts in the public domain (which means lots of great literary and historical texts published after 1925). 

!curl -O http://www.gutenberg.org/files/1952/1952-0.txt

!wget http://www.gutenberg.org/files/1952/1952-0.txt

#PowerShell C:\Users> wget http://www.gutenberg.org/files/1952/1952-0.txt -OutFile The-Yellow-Wallpaper.txt

%ls

### Rename a file

| Mac / Chrome / Linux                            | Explanation                                                                                               | Windows PowerShell                                                                   |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| `mv` *original-filename* *new-filename*    | **m**o**v**e or rename a file or directory                                                                | `move` *original-filename* *new-filename* / `ren` *original-filename* *new-filename* |

%mv 1952-0.txt The-Yellow-Wallpaper.txt

%ls

### Check file sizes, lengths, and word counts

| Mac / Chrome / Linux                            | Explanation                                                                                               | Windows PowerShell                                                                   |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| `ls`                                       | **l**i**s**t the files and folders in your current **dir**ectory                                          | `ls` / `dir` / `Get-ChildItem`                                                       |
| `wc -w -l` *filename*                      | show how many **w**ords or lines in a file                                                                | `gc` *filename* \| `Measure-Object -Word –Line`                                      |

Combining the `-lh` flag with the `ls` command will show you the long format version (`-l`) of each file with the file sizes formatted in a human readable (`-h`) way. The long format version of the file will include the file's permissions, size, and date that it was last modified.

%ls -lh

The file sizes can be found in the fourth column. The file `The-Yellow-Wallpaper.txt` is shown as 50K or 50 Kilboytes. For a helpful breakdown of Bytes vs Kilobytes vs Megabytes vs Gigabytes, see Stanford professor Ashley Taylor's [CS101 course website](https://web.stanford.edu/class/cs101/bits-gigabytes.html).

|    Abbreviation                      | Size                                                                                              | 
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| B                         | Bytes                                                                          | 
| K                         | Kilobytes                                 | 
| M                         | Megabytes | 
| G                        | Gigabytes | 

Now let's check how many words are in "The Yellow Wallpaper." Combining the `-w` flag with the `wc` command will return the number of words in a file.

!wc -w The-Yellow-Wallpaper.txt

#PowerShell C:\Users> gc The-Yellow-Wallpaper.txt | Measure-Object –Word

Let's check how many lines are in "The Yellow Wallpaper."  Combining the `-l` flag with the `wc` command will return the number of words in a file.

!wc -l The-Yellow-Wallpaper.txt

#PowerShell C:\Users> gc The-Yellow-Wallpaper.txt | Measure-Object –Line

### Display the contents of a file

| Mac / Chrome / Linux                            | Explanation                                                                                               | Windows PowerShell                                                                   |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| `cat` *filename*                           | show all the contents of a file                                                                           | `cat` *filename* / `type` *filename*                                                 |
| `less` *filename*                          | show snippet of a file that allows you to scroll through the entire thing                                 | `more` *filename*                                                                    |
| `head` *filename*                          | show the first 10 lines of a file (change number of lines by adding `-*a number*` flag, e.g. `head -100`) | `gc` *filename* `-head 10`                                                           |
| `tail` *filename*                          | show the last 10 lines of a file (change number of lines by adding `-*a number*` flag, e.g. `tail -100`)  | `gc` *filename* `-tail 10`                                                           |

The `cat` command prints the whole file to your command line.

!cat The-Yellow-Wallpaper.txt

That's often too much text to handle at one time. So you can also look at the first 10 lines of the file with `head`.

!head The-Yellow-Wallpaper.txt

#PowerShell C:\Users> gc The-Yellow-Wallpaper.txt -head 10

Or by adding a flag with a number (`-50`), you can look at the first however many lines you want!

!head -50 The-Yellow-Wallpaper.txt

The same goes for looking at the end of a file with `tail`

!tail The-Yellow-Wallpaper.txt

#PowerShell C:\Users> gc The-Yellow-Wallpaper.txt -tail 10

### Searching inside files

| Mac / Chrome / Linux                            | Explanation                                                                                               | Windows PowerShell                                                                   |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| `grep` "search term" *filename* or *directory-name*       |      search for lines that include search term in file                                                                                                     | `findstr` "search term" *filename*                                                                 |

The `grep` command allows you to search for a search term(s) in a file or directory and return each line that contains the term. Combining the `-n` flag with the `grep` command will return the corresponding line number as well.

!grep "yellow" -n The-Yellow-Wallpaper.txt

#PowerShell C:\Users> findstr -n "yellow" The-Yellow-Wallpaper.txt

Combining the `--color` flag with the `grep` command will highlight the search term(s) in a color.

!grep "yellow" -n --color The-Yellow-Wallpaper.txt

Combining the `-wc` flag with the `grep` command will return the number of lines that contain the search term(s) in a file or directory.

!grep -wc "yellow" The-Yellow-Wallpaper.txt

!grep -wc "paper" The-Yellow-Wallpaper.txt

Combining the `-B` and `-A` flags with `grep` will return a specified number of lines before (`-B`) or after (`-A`) the line that contains the search term(s). This can be a way to get more context for a search term.

!grep "wallpaper" -B 2 -A 2 -n --color The-Yellow-Wallpaper.txt

___

## Further Resources

* The Launch School's [Introduction to the Command Line](https://launchschool.com/books/command_line/read/introduction)
* DHRI's ["Introduction to the Command Line"](https://github.com/DHRI-Curriculum/command-line)