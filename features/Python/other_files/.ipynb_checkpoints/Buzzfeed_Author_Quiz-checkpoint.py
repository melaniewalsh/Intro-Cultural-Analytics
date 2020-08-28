#!/usr/bin/env python

quiz_greeting_prompt = "✨Greetings!✨\n\nThis is a Buzzfeed-style quiz that will tell you where you might like to live based on your favorite author.\nPlease enter your favorite author from the following:\nStephen King, Virginia Woolf, James Baldwin, Stephenie Meyer.\n"


favorite_author = input(quiz_greeting_prompt)

if favorite_author == 'Stephen King':
    print("✨You'd probably like to live in a creepy hotel✨")
    
elif favorite_author == 'Virginia Woolf':
    print("✨You'd probably like to live in a room of your own in London✨")
    
elif favorite_author == 'James Baldwin':
    print("✨You'd probably like to live in a neighborhood with good jazz in NYC✨")
    
elif favorite_author == 'Stephenie Meyer':
    print("✨You'd probably like to live in a rainy town in Washington✨")
else:
    print("✨Sorry, I don't know her✨")
    
play_again = input("Play again? Y/N?")


while play_again == 'Y':
    favorite_author = input(quiz_greeting_prompt)
else:
    print('Goodbye!')