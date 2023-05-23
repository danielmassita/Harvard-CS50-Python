# CS50's Introduction to Programming with Python (CS50P) 2022 
# https://cs50.harvard.edu/python/2022/weeks/4/
# https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V
# https://youtu.be/MztLZWibctI

# https://cs50.harvard.edu/python/2022/notes/4/

"""Lecture 4
Libraries
Random
Statistics
Command-Line Arguments
slice
Packages
APIs
Making Your Own Libraries
Summing Up
"""



"""Libraries
Generally, libraries are bits of code written by you or others can you can use in your program.
Python allows you to share functions or features with others as “modules”.
If you copy and paste code from an old project, chances are you can create such a module or library that you could bring into your new project.
"""



"""
Random
random is a library that comes with Python that you could import into your own project.
It’s easier as a coder to stand on the shoulders of prior coders.
So, how do you load a module into your own program? You can use the word import in your program.
Inside the random module, there is a built-in function called random.choice(seq). random is the module you are importing. Inside that module, there is the choice function. That function takes into it a seq or sequence that is a list.
In your terminal window type code generate.py. In your text editor, code as follows:

import random

coin = random.choice(["heads", "tails"])
print(coin)
Notice that the list within choice has square braces, quotes, and a comma. Since you have passed in two items, Python does the math and gives a 50% chance for heads and tails. Running your code, you will notice that this code, indeed, does function well!

We can improve our code. from allows us to be very specific about what we’d like to import. Prior, our import line of code is bringing the entire contents of the functions of random. However, what if we want to only load a small part of a module? Modify your code as follows:

from random import choice

coin = choice(["heads", "tails"])
print(coin)
Notice that we now can import just the choice function of random. From that point forward, we no longer need to code random.choice. We can now only code choice alone. choice is loaded explicitly into our program. This saves system resources and potentially can make our code run faster!

Moving on, consider the function random.randint(a, b). This function will generate a random number between a and b. Modify your code as follows:

import random

number = random.randint(1, 10)
print(number)
Notice that our code will randomly generate a number between 1 and 10.

We can introduce into our card random.shuffle(x) where it will shuffle a list into a random order.

import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
Notice that random.shuffle will shuffle the cards in place. Unlike other functions, it will not return a value. Instead, it will take the cards list and shuffle them inside that list. Run your code a few times to see the code functioning.

We now have these three ways above to generate random information.

You can learn more in Python’s documentation of random.
"""