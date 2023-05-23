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



"""
Statistics
Python comes with a built-in statistics library. How might we use this module?
average is a function of this library that is quite useful. In your terminal window, type code average.py. In the text editor window, modify your code as follows:

import statistics

print(statistics.mean([100, 90]))
Notice that we imported a different library called statistics. The mean function takes a list of values. This will print the average of these values. In your terminal window, type python average.py.

Consider the possibilities of using the statistics module in your own programs.
You can learn more in Python’s documentation of statistics.
"""



"""
Command-Line Arguments
So far, we have been providing all values within the program that we have created. What if we wanted to be able to take input from the command-line? For example, rather than typing python average.py in the terminal, what if we wanted to be able to type python average.py 100 90 and be able to get the average between 100 and 90?
sys is a module that allows us to take arguments at the command line.
argv is a function within the sys module that allows us to learn about what the user typed in at the command line. Notice how you will see sys.argv utilized in the code below. In the terminal window, type code name.py. In the text editor, code as follows:

import sys

print("hello, my name is", sys.argv[1])
Notice that the program is going to look at what the user typed in the command line. Currently, if you type python name.py David into the terminal window, you will see hello, my name is David. Notice that sys.argv[1] is where David is being stored. Why is that? Well, in prior lessons, you might remember that lists start at the 0th element. What do you think is held currently in sys.argv[0]? If you guessed name.py, you would be correct!

There is a small problem with our program as it stands. What if the user does not type in the name at the command line? Try it yourself. Type python name.py into the terminal window. An error list index out of range will be presented by the compiler. The reason for this is that there is nothing at sys.argv[1] because nothing was typed! Here’s how we can protect our program from this type of error:

import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
Notice that the user will now be prompted with a useful hint about how to make the program work if they forget to type in a name. However, could we be more defensive to ensure the user inputs the right values?

Our program can be improved as follows:

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
Notice how if you test your code, you will see how these exceptions are handled, providing the user with more refined advice. Even if the user types in too many or too few arguments, the user is provided clear instructions about how to fix the issue.

Right now, our code is logically correct. However, there is something very nice about keeping our error checking separate from the remainder of our code. How could we separate out our error handling? Modify your code as follows:

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
Notice how we are using a built-in function of sys called exit that allows us to exit the program if an error was introduced by the user. We can rest assured now that the program will never execute the final line of code and trigger an error. Therefore, sys.argv provides a way by which users can introduce information from the command line. sys.exit provides a means by which the program can exit if an error arises.

You can learn more in Python’s documentation of sys.
"""