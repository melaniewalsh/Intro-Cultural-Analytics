# Jupyter Tips & Tricks

## Code vs Markdown Cells

Jupyter notebooks are made up of cells, which can either contain code or [Markdown](https://www.markdownguide.org/getting-started/) text.

Markdown is a simple "language" that allows you to include formatting instructions directly in the text — bold, italics, headers, links, imgages, code, and more. Markdown is used all over the internet, such as on [Reddit](https://www.reddit.com/wiki/markdown#wiki_quick_reference) and on [GitHub](https://guides.github.com/features/mastering-markdown/).

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

## Edit Mode vs Command Mode
There are two modes in a Jupyter notebook: **Edit mode** and **Command mode**. You can use different keyboard shortcuts when in Edit vs Command mode.

from IPython.display import IFrame
IFrame("../videos/Edit-vs-Command-Mode.mp4", width='500', height='400')

If you click inside a cell, you switch to **Edit mode**. The cell will be outlined by a blue line.

If you click outside a cell in the sidebar or press `Esc`, then you switch to **Command mode**. The cell will no longer be outlined by a blue line. 

## Jupyter Keyboard Shortcut Cheatsheet

```{margin} For all possible commands
Press `Control` + `Shift` + `C` (Windows) or `Commmand` + `Shift` + `C` (Mac) to see all possible commands and shortcuts.
```


| Mac        | Jupyter Function                                                                                             | Windows       | 
|:---------------------------:|:-----------------------------------------------------------------------------------------------------------:|:---------------------------:|
| `Shift` + `Return`  | Run cell  (**Both modes**)                                            | `Shift` + `Enter`     |
| `Option` + `Return`                      | Create new cell below (**Both modes**)                                          | `Alt` + `Enter` 
| `B`                      | Create new cell below (**Command mode**)                                         | `B` 
| `A`                      | Create new cell above (**Command mode**)                                       | `A` 
| `D` + `D` (twice in a row)                      | Delete cell (**Command mode**)                                         | `D` + `D` (twice in a row)                    |
| `Command` + `Z`                      | Undo action inside cell (**Edit mode**)                                         | `Control` + `Z` 
| `Z`                      | Undo action outside cell (e.g., undo deletion of a cell) (**Command mode**)                                         | `Z`  
| `Shift` + `M`                     | Merge cells (**Command mode**)                     | `Shift` + `M`                      | 
| `Control` + `Shift` + `-`                   | Split cell into two cells (**Edit mode**)   |         `Control` + `Shift` + `-`   |                          
| `Tab`                      | Autocomplete file/variable/function name (**Edit mode**)     | `Tab`    |     \           
| `Shift` + `L`                      | Toggle line numbers for code (**Command mode**)     | `Shift` + `L`    |        
| `M`                      | Switch cell to Markdown (**Command mode**)     | `M`    |      
| `Y`                      | Switch cell to Code (**Command mode**)     | `Y`    |      
| `X`                      | Cut cell (**Command mode**)     | `X`    |           
| `C`                      | Copy cell (**Command mode**)     | `C`    |           
| `V`                      | Paste cell (**Command mode**)     | `V`    |      
| `Control` + `/`                      | Comment out lines (**Edit mode**)     | `Command` + `/`    |   

## Tab Autocomplete

You can hit `Tab` to autocomplete a filepath or a function name. Typing out the correct file path isn't always easy, so tab autocomlete helps a lot!

from IPython.display import IFrame
IFrame("../videos/Tab-Autocomplete.mp4", width='800', height='400px')

## Enable / Disable Scrolling for Outputs

* Right-click to enable / disable scrolling for outputs for any given cell

If you produce a very long output, you can enable scrolling for that particular output, i.e., display a small preview of the output that allows you to scroll through the rest of the results. This feature can help keep your Jupyter notebooks from getting ridiculously long and unwieldy.

## Show File in Browser

* Right-click the file at the top and select "Show File in Browser"

If you lose track of where your Jupyter notebook is located on your computer (it happens!), right-click and select "Show File in Browser" to see where it is located in the file browser on the left-hand side of the page.

## Interrupt / Restart Kernel

* Go to Kernel --> Interrupt Kernel
* Go to Kernel --> Restart Kernel

If you run a cell, and it's taking ages to complete or seems to be stuck, you can *interrupt* the *kernel* to try to stop that particular process, and, if that doesn't work, you can *restart* the entire kernel.

```{warning}

Restarting the kernel will cause saved variables to be lost.
```

## More Resources

* [Jupyter Python Notebook Keyboard Shortcuts and Text Snippets for Beginners](http://maxmelnick.com/2016/04/19/python-beginner-tips-and-tricks.html)