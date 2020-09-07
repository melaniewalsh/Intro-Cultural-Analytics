# Functions

A *function* is way of bundling up code to perform specific tasks. It's kind of like making a little Python wind-up toy that runs on command.


<img src="https://www.tintoyarcade.com/image/cache/data/product/Images_5100_5199/TTA5100-Penguin-Windup-01-1000x1000.jpg" class="center" >

Functions are useful because they can help make your code more organized and save you from repetition. If you have to do some task over and over again, you don't want to write out the same code over and over again from scratch. 

We've encountered built-in Python functions many times already, including:
- `print()`
- `len()`
- `type()`  

These functions contain bundled up code that perform specific tasks whenever we call them.

## Define a Function

To make your own function, you use the keyword `def`, short for *define*, followed by your desired name for the function, parentheses (`()`) and a colon (`:`).

Then, on the following lines, you indent one tab over and write some code that you want your function to perform. 

def sing_beyonce_lyrics():
    print("Okay, okay, ladies, now let's get in formation, 'cause I slay")
    print("Okay, ladies, now let's get in formation, 'cause I slay")
    print("Prove to me you got some coordination, 'cause I slay")
    print("Slay trick, or you get eliminated")
    return 

Finally, you complete the function with a `return` statement. Sometimes you will want to `return` a specific value but here we're not returning anything.

If you don't indent the line following the definition of the function, you will get an error. Behold the importance of the indent:

def sing_beyonce_lyrics():
print("Okay, okay, ladies, now let's get in formation, 'cause I slay")
print("Okay, ladies, now let's get in formation, 'cause I slay")
print("Prove to me you got some coordination, 'cause I slay")
print("Slay trick, or you get eliminated")
    return 

## Call a Function

To use or "call" a function, you simply type the name of the function with parentheses.

sing_beyonce_lyrics()

def sing_happy_birthday():
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print("Happy Birthday dear human life form")
    print("Happy Birthday to you")
    return 

sing_happy_birthday()

## Add Parameters/Arguments

You can add "parameters" to your functions—or values that are required by your function—by putting parameter names inside the parentheses.

For example, if we want to personalize our birthday song function to include a specific person's name, we can add the parameter `personalized_name` inside the parentheses, which will require a personalized name to be passed to the function. The thing you pass to the function is called an "argument." 

- parameter = `personalized_name` (thing that requires a value for the function) 
- argument = "Beyonce" (actual value passed to function)

Since parameters and arguments are so interrelated, they're sometimes confused for each other. You can read [Python's official distinction here](https://docs.python.org/3.3/faq/programming.html#faq-argument-vs-parameter).

def sing_personalized_happy_birthday(personalized_name):
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print(f"Happy Birthday dear {personalized_name}")
    print("Happy Birthday to you")
    return 

We're using whatever name gets passed to the function inside an f-string: `f"Happy Birthday dear {personalized_name}"`

Once you set a parameter that requires an argument, you have to pass something inside the function for the function to run. So if we run `sing_personalized_happy_birthday()` as we did with `sing_happy_birthday()`, it won't work.

sing_personalized_happy_birthday()

This error is telling us that we have to pass in a value or "argument."

sing_personalized_happy_birthday("Beyonce")

sing_personalized_happy_birthday("Carly Rae Jepsen")

sing_personalized_happy_birthday(#Insert Your Name Here)

## Keyword Arguments

There's another way that you can require arguments in a function, which is with *keyword arguments*. Before we were using "positional arguments," where the function automatically knew that "Beyonce" was the `personalized_name` argument simply because "Beyonce" was in the right position. (There was only one argument required, so, duh.)

But you can also explicitly define your arguments with keyword arguments that use an `=` sign, which can become more useful if you have multiple parameters. This can also be a way of setting default values in your functions.

def sing_keyword_happy_birthday(to_name='Beyonce', from_name='Info 1350'):
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print(f"Happy Birthday dear {to_name}")
    print("Happy Birthday to you")
    print(f"\nSincerely, \n{from_name}")
    return 

For example, if we don't pass in any arguments into this function, it will use the default arguments.

sing_keyword_happy_birthday()

But if we set the keyword arguments to different values—even if we switch the order or position of the arguments!—the function will know which arguments they're supposed to be.

sing_keyword_happy_birthday(from_name="Big Bird", to_name="Cookie Monster")

## Return Values

In all of the examples above, we weren't returning any specific value, just using `print()` statements. But sometimes you want a specific value out of your function. For example, if we want to make a function that transforms a bit of text into very loud-sounding text, then we'll want to `return` that loud-sounding text.

def make_text_shouty(text):
    shouty_text = text.upper()
    return shouty_text

make_text_shouty("I like tacos")

def make_text_shoutier(text):
    shouty_text = text.upper()
    shoutier_text = shouty_text + '!!!'
    return shoutier_text

make_text_shoutier("I like tacos")

def calculate_dog_years_age(age):
    dog_years_age = age * 7
    return dog_years_age

calculate_dog_years_age(52)

## Your Turn!

Make a function called `make_text_whispery` that transforms text to lower case

#Your Code Here
    whispery_text = #Your Code HEre
    return #Your Code Here

Now insert the string "I AM WHISPERING" into `make_text_whispery`

#Your Code Here