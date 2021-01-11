# Topic Modeling — Set Up

In these lessons, we're learning about a text analysis method called *topic modeling*. This method will help us identify the main topics or discourses within a collection of texts or within a single text that has been separated into smaller text chunks.

This page describes how to set up the packages and programs that you'll need if you want to start topic modeling on your own computer. If you want to topic model without installing anything, however, you can skip ahead and explore these Jupyter notebook topic modeling lessons in the cloud. The notebooks already have the necessary requirements installed.

## MALLET & Little MALLET Wrapper

For our topic modeling analysis, we're going to use a tool called [MALLET](http://mallet.cs.umass.edu/topics.php). MALLET, short for **MA**chine **L**earning for **L**anguag**E** **T**oolkit, is a software package for  topic modeling and other natural language processing techniques. It's maintained by David Mimno, a Cornell professor in Information Science. Go Big Red!

MALLET is great, but it's written in Java, another programming language, which means that we have to install Java before we can use it. It also means that MALLET isn't typically ideal for Python and Jupyter notebooks.

Luckily, another Cornellian, Maria Antoniak, a PhD student in Information Science, has written a convenient Python package that will allow us to use MALLET in this Jupyter notebook after we download and install Java. This package is called [Little MALLET Wrapper](https://github.com/maria-antoniak/little-mallet-wrapper).

Note: A "wrapper" is a Python package that makes complicated code easier to use and/or makes code from a different programming language accessible in Python.

## Download and Install Java Development Kit

But first, we have to install Java, specifically the Java Development Kit.

Go to the Java Development Kit download page, find your operating system, and click on the corresponding download link: https://www.oracle.com/java/technologies/javase-jdk14-downloads.html

- Linux -> Linux Compressed Archive
- Mac -> macOS Installer
- Windows -> Windowsx64 Installer

Then open or unzip the file and follow all the prompts. You can use all the suggested defaults.

## Tell Your Computer Where to Find Java

Now that we have the JDK downloaded, we have to tell our computers where to find it. For Mac/Chrome/Linux users, we have to set up a special ["environment" variable](https://launchschool.com/books/command_line/read/environment#environmentvariables) called `JAVA_HOME` and give it the file path where we just downloaded our Java Development Kit. For Windows users, we have to edit the special environmental variable called `PATH` and add the file path of the JDK.

Note: "Environment" variables are kind of like Python variables, except they exist in your whole computer environment. The Launch School has a helpful chapter on [environment variables](https://launchschool.com/books/command_line/read/environment#environmentvariables) and the [PATH](https://launchschool.com/books/command_line/read/environment#path) variable.

###  Mac

To set up the `JAVA_HOME` environment variable on a Mac, you can run the following on the command line. The line of code adds your `JAVA_HOME` variable to a file called "bash_profile", which is where environment variables are stored.

!echo "export JAVA_HOME=$(/usr/libexec/java_home)" >> ~/.bash_profile

To immediately update your "bash_profile," run:

!source ~/.bash_profile

Then, to test whether Java installed correctly, run `javac` on the command line. If you get a list of options, as below, then you've installed the JDK properly. If it says the command is not recognized, then you don't have JDK set up yet.

!javac

### <img src=https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Windows_logo_-_2012_derivative.svg/1024px-Windows_logo_-_2012_derivative.svg.png width=20 align='left'> Windows 

To edit the `PATH` variable on a Windows computer, follow the instructions below:

- Open Search and type "advanced system settings"
- In the shown options, select the "View advanced system settings" link
- Under the Advanced tab, click "Environment Variables"
- Under "System variables," click the variable "PATH" and then click "Edit"
- Click "New" and add the file path to the JDK (e.g. `C:\Program Files\Java\jdk13.0.2\bin`)

For more Windows installation help, see Prof. Paul Vierthaler's video tutorial ["Practical Python for DH: Topic Modeling Software Install"](https://youtu.be/2C3cDEd7h4o?t=224).

Now restart your PowerShell. To test whether java is installed, run `javac` in the PowerShell. If you get a list of options, then you've installed the JDK properly. If it says the command is not recognized, then you don't have it yet.

!javac

### Chrome / Linux

To set up the `JAVA_HOME` environment variable on a Linux machine or a Chrome computer running Linux, you can run the following on the command line. The line of code adds your `JAVA_HOME` variable to a file called "bashrc", which is where environment variables are stored.

Make sure to change `/fill-in-the-path/to/your-java_installation` to the file path where your JDK actually exists below:

!echo "export JAVA_HOME=/fill-in-the-path/to/your-java_installation/bin" >> ~/.bashrc

To immediately update your "bash_profile," run:

!source ~/.bashrc

To test whether java is installed, run `javac` on the command line. If you get a list of options, as below, then you've installed the JDK properly. If it says the command is not recognized, then you don't have it yet.

!javac

## Download and Unzip MALLET

Now we need to download the MALLET package. To download MALLET, click the following link http://mallet.cs.umass.edu/dist/mallet-2.0.8.zip or find the link on the [MALLET home page](http://mallet.cs.umass.edu/download.php). Once the zip file downloads, unzip it.

If you're using a Mac, move the "mallet-2.0.8" directory into your home folder.

*Note: To open your "home" folder, open "Finder" and type `Cmd` + `Shift` + `H`. To move one directory up, type `Cmd` + `↑`. Now, if you want to bookmark your home folder so you can find it more easily in the future, simply drag and drop your home folder to the sidebar.*

If you're using a Windows computer, move the "mallet-2.0.8" directory int your `C:\` drive. 

### <img src=https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Windows_logo_-_2012_derivative.svg/1024px-Windows_logo_-_2012_derivative.svg.png width=20 align='left'> Heads Up Windows Users! 

You need to complete one more step. You need to once again tell your computer where MALLET is located:

- Open Search and type "advanced system settings"
- In the shown options, select the View advanced system settings link
- Under the Advanced tab, click "Environment Variables"
- In the User variables section, click "New"
- For the Variable name, type `MALLET_HOME`. For the Value, type the path to your MALLET: `C:\mallet-2.0.8`. Then click OK
- Click OK and click Apply to apply the changes

For more Windows help, see Prof. Paul Vierthaler's [topic modeling tutorial](https://youtu.be/2C3cDEd7h4o?t=107).

To test whether MALLET works on your computer, type in the file path for MALLET on the command line and `import-file`.

If it's working, then you'll get a message that says "A tool for creating instance lists of feature vectors from comma-separated-values" and a list of options.

!~/mallet-2.0.8/bin/mallet import-file

## Install Little MALLET Wrapper

Finally, we're going to install the Python package [little_mallet_wrapper](https://github.com/maria-antoniak/little-mallet-wrapper). To install it, run `pip install little_mallet_wrapper`, as below.

!pip install little_mallet_wrapper

Since Little MALLET Wrapper also uses the data visualization library `seaborn`, we're also going to `pip install seaborn`:

!pip install seaborn

## You're Ready! 🥳
