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



"""
Packages
One of the reasons Python is so popular is that there are numerous powerful third-party libraries that add functionality. We call these third-party libraries, implemented as a folder, “packages”.
PyPI is a repository or directory of all available third-party packages currently available.
cowsay is a well-known package that allows a cow to talk to the user.
Python has a package manager called pip that allows you to install packages quickly onto your system.
In the terminal window, you can install the cowsay package by typing pip install cowsay. After a bit of output, you can now go about using this package in your code.
In your terminal window type code say.py. In the text editor, code as follows:

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
Notice that the program first checks that the user inputted at least two arguments at the command line. Then, the cow should speak to the user. Type python say.py David and you’ll see a cow saying “hello” to David.

Further modify your code:

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
Notice that a t-rex is now saying “hello”.

You now can see how you could install third-party packages.
You can learn more on PyPI’s entry for cowsay
You can find other third-party packages at PyPI
"""



"""
APIs
APIs or “application program interfaces” allow you to connect to the code of others.
requests is a package that allows your program to behave as a web browser would.
In your terminal, type pip install requests. Then, type code itunes.py.
It turns out that Apple iTunes has its own API that you can access in your programs. In your internet browser, you can visit https://itunes.apple.com/search?entity=song&limit=1&term=weezer and a text file will be downloaded. David constructed this URL by reading Apple’s API documentation. Notice how this query is looking for a song, with a limit of one result, that relates to the term called weezer. Looking at this text file that is downloaded, you might find the format to be similar to that we’ve programmed previously in Python.
The format in the downloaded text file is called JSON, a text-based format that is used to exchange text-based data between applications. Literally, Apple is providing a JSON file that we could interpret in our own Python program.
In the terminal window, type code itunes.py. Code as follows:

import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())
Notice how the returned value of requests.get will be stored in response. David, having read the Apple documentation about this API, knows that what is returned is a JSON file. Running python itunes.py weezer, you will see the JSON file returned by Apple. However, the JSON response is converted by Python into a dictionary. Looking at the output, it can be quite dizzying!

It turns out that Python has a built-in JSON library that can help us interpret the data received. Modify your code as follows:

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))
Notice that json.dumps is implemented such that it utilizes indent to make the output more readable. Running python itunes.py weezer, you will see the same JSON file. However, this time, it is much more readable. Notice now that you will see a dictionary called results inside the output. Inside that dictionary called results there are numerous keys present. Look at the trackName value in the output. What track name do you see in your results?

How could we simply output the name of just that track name? Modify your code as follows:

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])
Notice how we are taking the result of response.json() and storing it in o (as in the lowercase letter). Then, we are iterating through the results in o and printing each trackName. Also notice how we have increased the limit number of results to 50. Run your program. See the results.

You can learn more about requests through the library’s documentation.
You can learn more about JSON in Python’s documentation of JSON.
"""



"""
Making Your Own Libraries
You have the ability as a Python programmer to create your own library!
Imagine situations where you may want to re-use bits of code time and time again or even share them with others!
We have been writing lots of code to say “hello” so far in this course. Let’s create a package to allow us to say “hello” and “goodbye”. In your terminal window, type code sayings.py. In the text editor, code as follows:

def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")
Notice that this code in and of itself does not do anything for the user. However, if a programmer were to import this package into their own program, the abilities created by the functions above could be implemented in their code.

Let’s see how we could implement code utilizing this package that we created. In the terminal window, type code say.py. In this new file in your text editor, type the following:

import sys

from saying import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
Notice that this code imports the abilities of goodbye from the sayings package. If the user inputed at least two arguments at the command line, it will say “goodbye” along with the string inputed at the command line.
"""



"""
Summing Up
Libraries extend the abilities of Python. Some libraries are included by default with Python and simply need to be imported. Others are third-party packages that need to be installed using pip. You can make your own packages for use by yourself or others! In this lecture, you learned about…

Libraries
Random
Statistics
Command-Line Arguments
Slice
Packages
APIs
Making Your Own Libraries
"""



"""
[MUSIC PLAYING] DAVID MALAN: All right, this is CS50, Introduction to Programming with Python. My name is David Malan, and this is our week on library. So libraries are generally files of code that other people have written that you can use in your own programs or a library's code that you've written that you can use in your own program, but maybe not just this program, but another and another as well. 

So Python supports exactly this idea. This ability to share code with others, share code across your own projects. And it does so by way of what it calls module. A module in Python is just a library that typically has one or more functions or other features built into it. 

Generally, the purpose of a library or a module specifically is to encourage reusability of code if you find yourself using the same types of functions again and again, the same functionality. If you find yourself copying and pasting from an old project into your new project, odds are there's an opportunity there to factor out that code that you keep copying and pasting that you keep reusing and put it into a library that you can then load into your programs moving forward so as to not just copy and paste it and have all these different copies all over. 

So what are some of the modules or libraries that Python comes with? Well, Python comes with a random library literally, which is to say that when you install the Python interpreter on your Mac or PC or somewhere in the cloud, not only do you get Python, you get a whole bunch of modules as well. 

Now, these modules provide you with functions that you don't have access to just by default like you do print and input. Print and input and other such functions just work in Python. But sometimes functions are tucked away in these modules, so you have to be more deliberate about loading them into the computer's memory. 

So somewhere on the computer's hard drive, once you've installed Python, there is also, it turns out a file, probably called random.py that someone else wrote probably long ago but that you have access to. And in that random.py file, there's probably one or more functions that you yourself can use in order to do things randomly. 

That is to say how could you flip a coin in a program in Python? How could you pick a random number between 1 and 10 in Python? Well, you need a bit of randomness. And while you could figure out mathematically how to write functions like that yourself, it's a lot easier to stand on the shoulders of others who've already solved that problem for you so you can focus on the problem that you yourself want to solve. 

So for documentation on most any Python module, you go to the official Python docs. And you go to a URL like this where the documentation for that specific module lives. And within the documentation, you'll see a list of the functions or other functionality that some module provide. 

But how do you go about loading a module into your own program so that you can use the functions in that module? Well, we need a new keyword in Python and namely it's import. The import keyword in Python allows you to import the contents of the functions from some module in Python. 

Well, how might I go about using this in practice? Well, let me propose that there exists in that random module this function among others. So I have copied and pasted from the documentation this summary of a function called Choice. 

Now, the function exists in the random module, so to speak, not a random module, the random module. And so generally the documentation describes it fully like this. random.choice is how you would technically call this function, though, we'll see alternatives to that. 

In parentheses, there is a parameter called S-E-Q for sequence. And sequence generally means a list or something that is list-like if you have a list of numbers or strings or anything else. And the documentation elaborate. Well, how can I go about using this function to solve, perhaps, a familiar problem? 

Well, let me go ahead and open up VS Code here. And let me propose that we implement a program that simulates flipping a coin. A coin that in the US has heads or tails, the idea of which is to pick a decision with 50/50 probability. 50% probability of heads, 50% probability of tails. Or you can use some other mechanism like that. 

Well, let me go ahead and open a program with code called generate.py because I want to start generating a whole bunch of random information. The first of which is just going to be a coin toss. Now, how do I go about using that function? 

Well, I first have to import the random library. So literally the first or among the first lines of my file should be import random. And that just gives me access to all of the functions in that specific module. Now, suppose I want to flip a coin. Well, I can do random.choice per the documentation a moment ago. And that again takes a sequence. 

What's a sequence? It's a list or something that's list-like. And we know about lists. We've used lists to iterate over numbers. We've used lists to iterate over students at Hogwarts. Let's go ahead now and iterate over just a list of two sides of a coin, "heads," quote, unquote, or tails. 

Now, I could call these anything I want. These are my string. I just want to simulate a tossing a coin. So I'm just going to say in all lowercase, heads and tail. But notice the syntax. I have "heads" and "tails" in double quotes. That's because they're strings. I could also use single quotes so long as I'm consistent. There's a comma between them, which means the list has two elements. They're square brackets to the right and the left, which indicates that this is indeed a list. That's the syntax recall for defining a list in Python. 

And then lastly, there's something more familiar. There's the parentheses outside of those square brackets. But those are just the parentheses that belong to the Choice function and specify where its parameter gets passed in. But again, unlike past function, I have to specify what module this function is in at least for now. And so I do random.choice to call the specific function. 

All right, well, it's one thing to flip a coin picking between those with 50% probability. And that's what random.choice does. It takes in a list, and it returns to one of those values randomly with equal probability. Because I've passed in two items, I've got a 50/50 chance. If I passed in three items, it'd be a 33% chance for each of those items and so forth. Python does the math for you. 

But I want to store the value of this in a variable. So let's define a variable called coin equals whatever the return value is. So this is indeed like flipping a coin. I'm going to store in a variable called coin, whatever that value is, heads or tails. And now, just so I can see what's going on, let's go ahead and print out the value of that string coin 

All right, let me go ahead now and run this program in my terminal window. Python of generate.py, Enter. And it looks like the first coin toss was the heads. Let's go ahead and run it again. And it looks like it was heads again. Maybe you want to chime into the chat here. 

If I run it a third time, what's it going to be this time? If you want to type your thoughts in the chat, you might think there's a bug here. But this is probability in action. If I go ahead and hit Enter a third time there, it's actually now tails And again, tails and again tails and again tails and again tails and again heads. 

Now, if we did this an infinite number of times, it would indeed work out to be 50/50. If we only do it a few times, it might not work out as cleanly. But that's how probabilities indeed work. 

All right, so I've got that now working. Could I have implemented this in a different way? Well, let me show you an alternative to actually using the import keyword alone and let me introduce the keyword from in Python. So from is a keyword in Python that you can use when importing functions from a module, but it allows you to be a little more specific than import alone. 

So if I go back to my code here, it's worth noting that what technically I'm doing here by importing random is I'm technically importing everything that's in that module. So not just the function called random.choice but a few other functions as well. So instead of using this line of code at the top of my file, import random, which will technically give me access to all of the contents they're in, a downside of that is that I have to type in random.choice, random.this, random.that because all of the functions I'm calling have to be associated with the scope of that module. 

Well, suppose that I just want to call the function as its name, choice. I can do that as well. Let me replace this first line here with from random import choice. And what this does effectively is it loads the function's name choice into my current namespace into the scope of the file I'm working in. 

What that means is that I now no longer have to specify which choice function I mean. I can just say choice. And so it loads it into the local namespace that is into my local vocabulary, if you will, so I can just now say choice. This might be advantageous in what cases, do you think? 

When might you want to import the name of the function explicitly like this as opposed to just saying random.choice-- random.choice throughout your code when calling a function? Any instincts here for this alternative import using from? 

AUDIENCE: Hello, I'm Mohammed Omar from Egypt. And maybe if we have a variable that its name is basically like choice if I have a variable called the choice. So I need to differentiate which trays I choose. So I'm going to choose random data choice. 

DAVID MALAN: Yeah, really good instincts. By using the first approach by just importing random, you're making sure that all of its contents are associated with or scoped to the random module so that you can have your own choice function. You can have your own choice variable. You can use the same names as all of the functions or variables that are stored inside of that file without them colliding, so to speak. And this is a good thing. 

In older languages, it was the case that if you imported someone's library, you better hope that you're not using the same functions or variables as they are because you might in fact have some kind of conflict. Python and certain other languages allow you to scope the names of those functions and variables to the file or the module that they come from. So that's a good thing. 

But honestly, this is such a short program. Or equivalently, maybe I'm using the choice function in so many places calling random.choice, random.choice, random.choice. It's just making my code longer and longer and longer. 

Marginally so, but hey, just getting ugly and annoying, I can simply import choice and now tighten up my code a little bit. So as with so many decisions in the past, there's not necessarily one right approach or another. It depends. But I think for those very reasons, sometimes it's better to do what we did the first time, which is only import the module so as to retain the scope therein. 

Well, let me propose that we transition to another function that comes with Python's random module. And that's this here from the documentation randint. It's a bit hard to say, but it implies get back a random int. And if you read the documentation, it's a random int that's between A and B inclusive. 

So if you were to pass in 1 for A and 10 for B, you would get back a number between 1 and 10 inclusive, including the 1 and including the 10 potentially. Each with a 10% probability. So how might I go about using a program like this? Well, let me come back to my generate the py file. And why don't we go ahead and try generating a random number between 1 and 10? 

You might do this frequently in the real world. When you just want someone to pick a random number, you tell them as much in the human response. Let's get the computer to do the same here. Let me go ahead and delete my two lines of code at the bottom but keep my import random. 

And let's go ahead and define a variable this time called number, set it equal to the return value of random.randint and now passing A, a value of 1 and B, a value of 10. And now, let's go ahead and print the number. I'm going to go ahead in my terminal window and run Python of generate.py and hit Enter. 

4. A Python of generate.py and hit Enter. 8, again, 9, again, 7, again, 10, again, 2, again. And we can do this all day long. And if we add all of those up, they should end up being with 10% probability each. 

Now, how might you use this information? Well, maybe we're playing a guessing game. Or maybe we're trying to randomize the behavior of some character in the game. You can imagine using very simple building blocks like this just spicing up your program by getting it to do things a little less predictably because you're choosing these values seemingly randomly. And you're deferring to Python to actually do the generation of these numbers using its own algorithms and its own math. 

Well, what more could we do here? Let me propose that we introduce another function that comes from this random library. Yet, another that you yourself don't have to implement, shuffle. If you read the documentation for shuffle in the same random module, you'll see that it takes in a list, for instance, of values and just shuffles them up. It randomize them like a deck of cards. 

Here, you might shuffle them so as to put them into seemingly random order. Well, how do I use this based on this function's name? Well, let me propose that we go back to VS Code here. And let me go ahead and this time do the following. Because I need to shuffle something like a deck of cards, let me go ahead and not just import random. But let me give myself a variable called cards that's going to be of type list. And just so I have something to shuffle, I don't need all 52 cards in a typical deck. 

I'm just going to shuffle three cards. A Jack, a Queen, and a King. I could call those strings anything I want, but I just wanted a list of some values so as to shuffle them up. That is randomize the order therein. Well, how does this now work? If you read the documentation for random.shuffle, you'll see that it shuffles the argument in place. 

That is unlike many of the functions we have seen. It doesn't return to you a value that contains the shuffled cards in this case. It actually shuffles the list it's given itself. So what this means for my code is that I need to do something like this-- random.shuffle and pass in the variable containing those cards. 

And then on a final line here, how might I go about printing the cards? Well, I could do this, and I could say print card. But if I do that, I'm actually going to see Python syntax for lists. And it's just going to format in its own way using commas and the like. I want to print these cards out one at a time just because I think it'll look a little better so we can use some of our syntax from loops and say something like this-- for card in cards, go ahead and print out the current card. 

So what's now happening here? Line three, I'm defining a list of three cards in this order-- Jack, Queen, King. I'm then shuffling those same cards on line four. And then on line five, I'm using a for loop for each of the cards in that list printed out one at a time and because I'm using print one line at a time. 

Well, let's see the results. Down here in my terminal window, I'm going to run Python of generate.py and hit Enter. Queen, King, Jack seemingly shuffled because that's not the order I defined earlier. Let's do it again. Queen, King, Jack. Hmm, OK, that happens to be the same. But let's see. This could just be bad chance. 

There we go. Jack, Queen, King. Doesn't look like it's shuffled, but at least we're getting back different orderings now. Again, Jack, Queen, King. Hmm, not so good. Jack, Queen, King. Not so good. This is someone you probably want to play against with cards. Queen, Jack, King, there we go. 

But of course, we only have three cards here. So there's not that many permutations we might see. And if we do this over time, we will see all of them. But if we had, of course, 13 or 52 cards, we'd see a lot more permutations instead. 

So we have now these three ways to generate random information. One, a simple coin toss if you want to start some kind of athletic event. One, pick a number between 1 and 10 if you want to decide something based on that. And now, using shuffle, we can even take in a list of things and shuffle them about so that we get some kind of random behavior. Well, let me pause here and see if where there's any questions yet on random, on modules, or any of these three functions. 

AUDIENCE: Yeah, can we increase or decrease the probability of cards if we want to? For example, there are three. There is a 33% chance of probable B. So is there any chance to increase or decrease the probability? 

DAVID MALAN: Can you set these probabilities not using these same functions? Can you set the probabilities? But you can absolutely implement some of your own functions or use more sophisticated functions that do exist in this library and others to exercise more control. 

These are meant to be very user-friendly and simple functions, certainly the ones we looked at, that give you equal probability for all of those. But absolutely you could skew things, though, hopefully, if you're implementing a gambling game or the like, you're not actually making some cards more probable than others. 

Allow me to turn back now to our implementation here of this randomness and consider how we might leverage other types of functionality that aren't necessarily in this specific library here. Well, it turns out that Python also comes with a statistics library. And this contains all sorts of functions for doing things more statistical in nature, namely calculating means or medians or modes or other aspects of a data set that you might want to analyze. 

So how might we use the statistics module in Python? Well, we might first just take a look at it's documentation like any other module in Python. And we'll see within that library that there's a whole bunch of function. And one of those functions is one that's quite simple. It's average. A function that allows you to calculate the average of some numbers that you've passed in. 

Let me go ahead and in VS Code in my terminal window, open up a new file called average.py. And at the top of this file, I'm going to import a different library this time, namely the statistics module in Python. And now, I'm going to go ahead and call a function that I know comes in that module, namely mean for the average of some values. And I'm going to call statistics.mean. 

And I'm going to pass into this function mean, a list of some values. And let's suppose that I'm quickly trying to calculate what my current grade average is in school. And I did really well on my first test. And I got 100%. And on my second, I did well but not as well. And I got a 90. And ironically, I'm not very good with math. So I'd like to figure out what my average now is between those two tests. 

So let me go ahead now and in this list, type in the number 100, comma, 90, thereby passing in a list of two values, two INTs, 190. And outside of those are the parentheses because, of course, this is now the argument I'm passing to the function called mean. And this function mean is in the module called statistics. 

Well, it's not that interesting to just calculate the mean if I don't actually see what it is. So let me additionally pass the return value of that mean function to the print function as usual. Let me now in my terminal window in VS Code, type in Python of average.py and hit Enter. And voila, as you might expect, my average is 95%. 

So the difference here is that I'm just using a different module that still comes with Python. But I need to import it instead of, for instance, the random module instead. And this time, I know from the documentation that there exists a function called mean. 

Well, it turns out there's even more functionality that comes with Python and that comes with other modules in Python. And there's this feature generally known as command line arguments. This is a feature, not just of Python, but of languages more generally that allow you to provide input not when prompted inside of a program as happens whenever we call the Python function input. 

But rather, there's this feature, command line arguments of programs, that allows you to provide arguments that is input to the program of just when you're executing at the command line. So up until now, for instance, recall that we've generally run Python of something.py. For instance, Python of hello.py. And I've never once really executed any words or phrases after the name of the file, but I could. 

In fact, when you're running programs in a command-like environment like we are, you can provide any number of words or numbers or phrases after the command that you're typing. And all of those will somehow be passed in as inputs to the program itself. You don't have to prompt the user for one thing at a time by manually calling that input function. 

So what does this mean in real terms? Well, let me go ahead back into VS Code here. And let me propose that we consider how we might leverage a certain module. I'm going to go ahead and create a file called name.py. And I'd like to use a new module this time that's going to give me access to values that have been typed at the command line. 

But what's this module going to be? Well, this one's going to be called sys. And sys, short for system, contains a whole lot of functionality that's specific to the system itself and the commands that you and I are typing. The documentation for this module is at this URL here. And it lists all of the various functions and variables and the like that come with that module. But we're going to focus on something a little more specific, namely this thing here. 

It turns out in the sys module in Python, there is a variable that just magically exists for you called argv. It stands for argument vector which is a fancy way of describing the list of all of the words that the human typed in at their prompt before they hit Enter. All of those are seemingly magically provided to you via Python in a variable called sys.argv. 

This variable is a list, which means that the first element is going to be the first word that you type. The second element is going to be the second word that you typed in, so forth. And by way of this list, then, can you figure out what words did the human actually type at the prompt and maybe use that to influence the behavior of your own program? 

So what does this mean now in real terms? Well, in this new tab called name.py, let me go ahead and import sys. Within that sys module is going to give me access to sys.argv, but how might I want to use it? Well, let's do this. Instead of writing a Hello World program that all of these times has just looked for the return value of input to figure out what the user wants me to print, let's go ahead and just expect the user to tell us when they run the Python program itself, what their name is. 

And suppose this time, I'd like to generate a whole bunch of name tags, initially just one. And in the US here, it's very common to wear a sticker on your lapel that says Hello, my name is David. So I want to print out some text that resembles that. The idea being maybe I could enhance this program someday to even send that text straight to the printer and dynamically generate those name tags. 

Well, let me go ahead now and do this. Let me go ahead and print out as always, Hello. But I'll say a little something more this time to make things more interesting. Hello, my name "is," quote, unquote. And then after that, I normally have been in the habit of calling input, storing the return value in a variable, and passing in the name of that variable here. 

But I'm going to instead jump right to this-- sys.argvbracket1. And that's it. I'm going to have a program here that says Hello, my name is followed by whatever is in sys.argvbracket1. And notice, this .argv again is a list. And recall from our discussion of loops and in turn list, we use this square bracket notation to get at the various elements inside of a list. 

All right, let me go down now into my terminal window and run Python of name.py. But this time, rather than just hit Enter and wait for the program to prompt me for my name, let me proactively just tell this program what my name is at the so-called command line. 

Here we go. D-A-V-I-D separated with a space from the name of the file so that now when I execute Python, name.py David, I see on the screen, voila, Hello, my name is David. So based on this demonstration alone, I think we can infer exactly what's going on in sys.argv even though it sounds certainly at first glance, rather complicated here. 

Let's look up. At sys.argv, I'm going to bracket1 here. So clearly, sys.argvbracket1 is storing D-A-V-I-D. But it's one. In the past when we looked at loops, recall that we said that they were zero index. That is the first element is zero. The next element is one. This next element is two and so forth. 

And yet, here I am treating it as though my name is at the start of the list one. Well, let me ask this question, what is probably in sys.argv of 0? What is probably in sys.argv of 0-- the very first element actually in that list? 

AUDIENCE: Oh, yeah. I think it's like in C, the name of program. 

DAVID MALAN: Indeed, it's indeed like in C. Another language is the name of the program. Well, if we consider what it was I typed, I certainly typed Python because that's the name of my interpreter. And we don't really need to know that because we're using Python itself. 

But after that, I did type two things. I typed name.py as I've done so many times any time I want Python to the interpreter program I've written. And it turns out by convention, what Python does is it stores in sys.argv the name of the file that you're executing or interpreting followed by any number of other words that you type. 

So all this time, we could have been accessing the name of the program, which frankly, isn't all that interesting. But we can also now access words that are typed after that prompt as well. But of course, if I don't type anything in, what might happen here? This might be naive of me to assume that there's always going to be something at location1 in sys.argv. 

Let me go ahead and try this. Python, name.py. And I'm not giving you my name because at this point, I might not even know that you want my name to be typed. So let me hit Enter now. And uh, oh, we see now an error. A so-called exception in Python, this one's a new one. This one's an index error that elaborates list index out of range. 

And turns out this is actually one of the most common mistakes in programming, whether you're using a list in Python or arrays or vectors in other languages, is to try to access some element that does not exist. You try to go too far to the left. Or you try to go too far to the right in this object that is just a list of some values. 

So of course, the mistake here is that I'm assuming there's going to be something at location1 when really, it's location0. That's the only one that has a value. But fixing this is not going to amount to doing bracket0 because now if I go ahead and rerun this program with no other words after name.py, it says Hello, my name is name.py, which is fine if we're making a name tag for the program, but that's not, of course, what my goal here is instead. 

So if the fix is not just to change the one to a zero, how else might I handle this error? How else might I handle this error? This index error that happens if the user just doesn't remember to or doesn't know to type their actual name at the prompt. 

AUDIENCE: We could always put an exception into the program, say, if there's nothing at location1, we just come out and say, OK, we haven't got parameter or something. But if there is, we continue along with the program. 

DAVID MALAN: Perfect. So if I might simplify, we can try to execute this line of code, except if there's an error, we'll deal with it in some other way. Now, ideally-- and once I'm a strong enough programmer, I would have anticipated this and written the following code from the get go. But when you're learning, it's certainly reasonable to see an error. Oh, I didn't realize I should detect that and then go back and improve your code. 

But of course, if you read the documentation, you ingrain some of the lessons learned from the past. You'll get into the habit of trying and checking for some of these exceptions yourself. So let me solve this in one possible way as you've proposed here. Let's try to handle this exception as follows. 

Let me go ahead now. And instead of just blindly calling this print line, let me try to print out Hello, my name is such and such, except if there is an issue, specifically an index error, then what do I want to go ahead and do? I'm going to say something like too few arguments. 

I could be more explanatory than that. But for now, I'm just going to explain to the user that they gave me too few arguments, too few words at the prompt. So now, it's still not going to work in quite the way I want. I'm still not going to be able to generate their name tag. But at least, they're not going to see some cryptic error message and think that they themselves broke the program. 

Let me go ahead now and run Python of name.py Enter and too few arguments. OK, let me go ahead now and do Python of name.py and type in my name, David. And now we're back in business. And I see that my name is on the screen too. 

But strictly speaking, I don't have to try to do this. I could actually be a little more defensive in writing this code. And maybe I could check whether or not the user has indeed provided a name or multiple names at the prompt so as to give them more refined error messages as well. 

So how might I do this? Well, me go and undo the exception handling I've added. And why don't I instead more modestly try to do this? Let me go ahead and introduce a conditional here. If the length of sys.argv is less than 2 or equivalently equal to just one value-- but I'll just stick with less than 2 for now, then go ahead and print out two few arguments. 

So I want ultimately two arguments. I want the name of the program at location0. And I want the name of the human at location1. So that's a total of two arguments. So if I have fewer than two arguments, let's tell the user with this print line, L if the length of sys.argv is say greater than 2, like they typed in too many words at the prompt, well, let's tell them, print, quote, unquote, "too" many arguments. Else if they did get it right, and they gave me exactly two arguments. Else, let's go ahead and print what I actually care about. 

All right, let me go down to my terminal window here and run Python of name.py and voila. Uh, oh, a completely different type of error. This one a syntax error, which we've seen in the past. Now, a syntax error recall is mea culpa, like, I messed up here. And I wrote invalid syntax. 

And so no amount of conditionals or exception handling's really going to catch this one. I need to go back and just get my program to work because it's not running at all. Well, let me go up here and see. Line four is the issue. And indeed, it looks like I have an unterminated string here. I need to go ahead and now add this double quote. 

So let me go ahead now. And with that red herring gone, let me rerun Python of name.py and hit Enter. And now, we see too few arguments. OK, maybe it wants my full name. Let me go ahead now and run Python of name.py, David Malan, typing in both words after the name of the file and hit Enter. And now, of course, it's too many arguments. 

Fine. Now, I'll oblige and do Python of name.py and just David. And there we have it. My name tag printed on the screen. So strictly speaking, we don't have to handle exceptions if we can be a little smarter about it and just check for the things that we're worried about, especially if we want to give the user more refined advice. 

We don't want to just tell them no, something went wrong or we don't want to pass. We want to tell them no, that's too few or no, that's too many. We have conditionals in our vocabulary already via which we can now express that. 

Well, let me pause here and see if there's any questions now on how we handled the error before with the index error or how now we're just proactively avoiding all index errors altogether by just checking first, is it too few? Is it too many? Or is it exactly what we want? 

AUDIENCE: Hi, yeah, thank you. So I was wondering, you touched upon using your full name. Is there a way going forwards that perhaps we have people that want their full names and want just their first name that we separate that into, oh, this person has full name. This person has just the one name? 

DAVID MALAN: Absolutely, and allow me to propose we come back to that support for multiple names. But indeed, we could do that. And I should note too, though, we can support full names right now if I do this. Instead of typing in David space Malan, which is problematic because again, by definition of how are argv works, each word ends up in a specific location in the list. 

But if I add quotes, single quotes or double quotes at the command line, now, Python will view this as two total things. The name of the file and this full name. And now, when I hit Enter, I don't see the quotes. The whole thing is passed in as my full name. And if I want to adapt this further for multiple people, we'll be able to do that as well. Other questions now on this version with if, elif, else, or on except before. 

AUDIENCE: Python. I want to ask you, can we use multiple else's statement? 

DAVID MALAN: Can you use multiple else's statements? No, else is the last catchall statement that you can have. You can have multiple elif statements in the middle but not multiple elses. 

AUDIENCE: [INAUDIBLE] 

DAVID MALAN: All right. All right, well, let's turn our attention back now to this code and see if we can't refine it a bit more by adding in some additional functionality that we get with modules like the sys module. One of the things I don't love about this version of the code even though arguably it is now correct is that the essence of my program, which is just to print out the name tag, is relegated to this else clause. And that's fine. 

Logically, it's correct, but generally speaking, there is something nice about keeping all of your error handling separate from the code that you really care about having all of these ifs, elifs, perhaps at the top of your code that are checking to make sure that all of the data's as expected. 

But then it would be nice if only for design sake not to hide in this else statement the actual code that you care about. I would prefer, for instance, to do something logically like this. I could check for errors up top. And then down here, print the name tag. 

It would be nice if those are distinct blocks of code all of which are here left aligned. But there's a problem with what I've just done here. Logically, what bug did I just introduce by getting rid of the else and introducing line 10 on its own with no indentation outside of the conditional? What bug have I just introduced? What mistake to be clear? 

AUDIENCE: Name error. 

DAVID MALAN: Ironically, it's a name error but not a name error exception. It's an error with my name, but I think you're frozen for me. It's going to raise an exception because even though I'm checking the length of sys.argv up top and even though I'm checking it again for being greater than 2, not just less than 2, but greater, I'm still then blindly and incorrectly assuming it's now going to exist. 

So just to be clear, if I run Python of name.py and I don't type any argument-- I've got too few-- I think I'm going to see that I have too few, but I'm also going to see that same exception. At the very top of my terminal window's output, there's my error message, too few arguments. But again, on line 10, I blindly proceed to still index into my list at location1 which does not exist. 

So it turns out there's a better way to handle errors like this, especially if you're writing a program in Python that's just meant to run briefly and then exit anyway. But maybe we could start to exit prematurely if the program itself just can't proceed. If the user has not given us the data we want, perhaps, we should just exit the program earlier than we might otherwise. 

So let me go ahead and do this. Let me go ahead and remove my comments so as to focus only on the code here. And let me propose that instead of just printing, quote, unquote, "too" few arguments, I'm going to use one other function that comes with the sys module. I'm going to go ahead and call sys.exit. 

And as the name suggests, it's going to do exactly that. With the system's help, it's going to exit my program then and there on line four. Why is that OK? Well, if you gave me too few arguments, I have nothing more to say to you, the user. I might as well exit a bit prematurely. And I can do this as well on line six. 

Let's go ahead and not just print that, but sys.exit, quote, unquote, "too" many arguments. Print out that message and just exit right there. Now, I can trust that by the time I get to line eight, every error condition has been checked for. And so it's safe for me to assume that there is in fact an item at location1 in sys.argv. 

So let me go ahead now and run this, Python of name.py, Enter, too few arguments. But I'm back at my prompt. Nothing more has happened. Let me run it again. Python of name.py David Malan with no quotes, Enter. Too many arguments is now printed here. Finally, Python of name.py just David, Enter. Hello, my name is David. 

So we have then in sys two forms of functionality. Now, we have access to this variable, sys.argv, this argument vector, that gives me all of the words that were typed at the prompt, including the program's own file name. And it turns out if we read further in the documentation, there's an exit function that can take different types of input. But if I pass out a string like this, it will indeed print that string for me and then exit from my program then and there. 

Questions now on exiting from programs like this. To be clear, all of this time once Python gets to the bottom of your file, it's going to exit anyway. So I'm using sys.exit now just to make sure that I exit earlier than otherwise. 

AUDIENCE: My question is about the sys that arg-- argv. So is that capable of accepting or taking multiple elements at once? Let's say, for example, Python name.py, David Malan. I'm a male, 20 years old. And if let's say I only want to access your name, which is at the first index. And then your age is, say, at the sixth index. Can I say sys.argv1 and another one for six to access what I just want? Is that both for sys.argv? 

DAVID MALAN: Short answer-- yes, I think if I understand your question correctly, whereby, you're proposing to have many words at the end of the command. And you want to access those individual words. Absolutely. At some point, it gets a little fragile, I would say, if you're typing so many words at the prompt that the order really matters. 

And so it turns out there's a lot of programs. And there's functionality in Python that can allow you to provide those values, like name or age or any number of other fields in any order you want, but a pass in a bit more information textually that tells the program how you want to use it. 

So in short, what you're describing is possible. And let me do a small incarnation of it as follows. Let me propose that we go back to my code here. And let's propose that we actually now want to support multiple values at the prompt. So there's going to be no such thing as too many arguments. Suppose that I want to generate name tags not just for David, but for David, for Carter, for Rongshin, for others in the group who all want their name tags as well. 

So I'm going to go ahead and do this. I'm going to get rid of my elif condition because I don't want to limit the maximum number of words that are typed at the prompt anymore. I instead want to iterate over every name at the prompt. So I'm going to say this. For arginsys.argv, go ahead and print out this time, arg. 

So what am I doing here? Well, even though the syntax is a little different, the idea's the same as before when we've had loop. I'm using a for loop to iterate over a list. The list in question here is sys.argv. Arg is a variable that I'm creating on the fly. The for loop is going to make sure that the first time through this loop, arg is set to the first word on the command line. 

The second time through the loop, Python's going to make sure that arg is now set to the second thing on the command line and so forth. That's just how a for loop works. It updates the variable for us. I don't have to call it arg. I could call it name so long as I change it to name in both places. But arg is reasonable if I'm iterating over arguments more generally. 

If I now run this program, though, unfortunately, there's a little bit of a bug. Even if I type in David and Carter and Rongshin, I'm not going to get just three name tags. In your mind, does anyone see the bug I'm about to trip over? It's not a huge deal if I've got enough name tags to go around. But I'm going to be wasting one because this is going to print not three, but four name tags, whereby, the first contains the name of the program itself. 

Maybe not a big deal. Maybe that's the sticker we don't bother handing out, but it's wasteful. And it does look wrong. So how could we get access to not all four elements of argv but just a slice of argv? And this is actually a technical term in Python and some other languages. To take a slice of a list means to take a subset of it maybe from the beginning, maybe the middle, maybe the end. But a slice is a subset of a data structure like a list. 

Well, how do I actually do this in code? Well, in Python, it's actually very easy to take a slice of a list that is a subset thereof. You can simply do this. At the end of the list name, sys.argv in this case, you can use square brackets. And then in those square brackets, you can specify the start and the end of the list that you want to retain. 

I want to start at element1, not zero. I want to start at element1, and I want to just go to the end. So I'm actually going to omit a second number altogether. It's not necessary to have a second number. But I do need that colon because this is going to give me a slice of the list. It's going to give me a slice of the list that starts at location1, not zero. And the colon and then a blank just means it's going to give me everything else. 

So this is in equivalently going to slice off the first element of the list and give me a new list that contains just those three human names, not the name of the file itself. Let me try running this again. I'm going to run Python of name.py, David Carter Rongshin. This time hopefully, I'm going to get three and only three name tags, hitting Enter. And indeed, I've done now just this. 

So again, using some relatively simple syntax in Python, we can use square brackets not just to go to specific elements like bracket0 or bracket1. We can also get subsets of the list, slices of the list by doing bracket something colon something where each of those some things is a number, the beginning or the end, and they're optional depending on whether you want all of them or just some. Any questions now on this version, which adds the loop and these slices with that new syntax? 

AUDIENCE: Can we slice starting from the end of the argument-- argument vector? 

DAVID MALAN: You can. You can slice something from the end of the argument vector. And this might blow one's mind a little bit. Let me go ahead and do this. Let's see. Let me go ahead and do negative one at the end. Using a negative number here and running the same command, we've just uninvited Rongshin from receiving a name tag here. So if you use a negative number, it has the effect of counting in the other direction from the end of the list. A good question there. Other questions now on slices, on looping over sys.argv? 

AUDIENCE: Hi, so I remember very early on when we were talking about only having two decimal places in float value. Is that in the same vein, like, because we use the code on 0.2F? Is that the same thing then? Why would the F be included then in the 0.2F as opposed to here when you just have the numbers? 

DAVID MALAN: A really good question. And it's just the short answer's that context matters. So there's only so many keys on our keyboard. And so we sometimes use the same symbols for different things. So what you're alluding to is the format code in an F string for actually formatting a number using a colon, using a period, using a number, using the letter F and so forth. And that is very specific to the F string feature of Python. 

This case has nothing to do with any of that syntax per se. This is just using a colon in a different context to solve this problem to implement a slice. The authors of Python could have chosen another symbol. But honestly looking down at my keyboard here, we don't have that many to choose from that are easy to type. So sometimes they have different meanings. A good question as well. 

Allow me to propose now, that we take things further and move away from using only those modules, those libraries that Python comes with to talk about more generally packages that exist. One of the reasons that Python is so popular and powerful these days is that there's a lot of third-party libraries out there as well, otherwise known as packages. 

Strictly speaking, Python itself has a term of art called a package, which is a module essentially that's implemented in a folder, not just a file but a folder. But more generally, a package is a third-party library that you, that I can install on our own Mac or PC or our cloud server and gain access to even more functionality that other people have implemented for us. 

Now, one of the locations you can get all of these packages is called the PYTI website, the Python Package Index which lives at this URL here. And this is a website that is searchable via the command line, as well as via the web, that allows you to download and install all sorts of packages. Even CS50 has some of its own packages in services like these. 

Now, there's a fun one out there that's a throwback to a command that's been around for years in command line environments called cowsay. Cowsay is a package in Python that allows you to have a cow say something on your screen. If curious to read up on it, its own documentation is on pi.py.org specifically at this URL here. 

But how do you actually get the package into your system? Well, technically, you could figure out how to download the file and maybe unzip it and put it into the right location on your Mac or PC. But nowadays, a lot of languages, Python among them, has what's called its own package manager. This one here called pip which is just one. 

So pip is a program that generally comes with Python itself, nowadays, that allows you to install packages onto your own Macs or PCs or cloud environment by just running a command. And then voila, you have access to a whole new library in Python that didn't come with Python itself. But now it's available on your system for you. 

Let's go back to VS Code here. And in my terminal window, I'm going to go ahead and type pip install cowsay. Now, what's going on here? Pip is the command, the package manager. And I want to install what package? The package called cowsay. I'm going to go ahead and hit Enter here. And after a little bit of output, it has successfully installed cowsay. 

Now, what does that mean? That means I can now go about importing this into my own code. Well, let's go ahead and see what this means. So let me go ahead and create a new file with code called say.py because I want something to be said on the screen. And in my new tab here, I'm going to go ahead and import cowsay, which presumably is now installed. 

I'm now going to import sys as well because I'd like to use some command line arguments in this program just so that I can run it quickly. And without using the input function, I can get the user's name immediately from the prompt. And let me go ahead and do this. I'm going to do a bit of error checking proactively this time. And rather than use less than or greater than, I'm this time going to say if the length of sys.argv does equal 2. 

So if the human is provided just the name of the program and their own first name, we're good to go. I'm going to do the following. I'm going to call a function called COW in the package called cowsay. And I'm going to pass in a string, hello, comma. And then as in the past, I'm going to pass in just one string because according to its documentation, it's not like print. I can't pass in comma this, comma that. 

I can only pass in one string. So I'm going to concatenate it the contents of sys.argv, bracket1. So long as then I type in my name David after the name of this program, it should end up in sys.argv1 in which case, this line five of code should concatenate hello with my name with a space in between. And apparently, a cow is going to say it. 

So let's see what happens here. Let me go ahead and clear my screen and increase the size of my terminal window. Let me go ahead and run Python of say.py and type my name David and Enter. There is the program called cowsay. 

It literally has a cow say something on the screen. And this is a throwback to a program from yesteryear that tended to come with a lot of systems. This is otherwise known as ASCII art. It's a textual way using just keys on your keyboard to print pictures of sorts on the screen. 

Now, we can really go down the rabbit hole here. And there's questionable academic value of doing so. So I'll do so just once. Turns out the cowsay package comes with other functions as well. One of those functions, for instance, is T-Rex. And if I now increase the size of my terminal window, we'll perhaps see where we're going with this. 

Let me now run again, Python of say.py. This time, let me not provide my name just to see if it's broken. It's still OK because we have that if condition if the length of sys.argv equals equals 2 and only if it equals equals 2, do we do anything. That's why we're not seeing anything here. 

Let me go ahead and cooperate now, say.py space David. And it's no longer a cow. But if I zoom out on my screen, a T-Rex. Why? Just because these are the things you can do once you know how to program. You can even package them up and make them freely available to others as open source software. For us, it's demonstrative of a feature more generally here namely being able to install these third-party packages and how you might do so in Python. 

Now, I'll leave this up on the screen for a moment and see if there's any questions about cows or Tyrannosaurus rex's or packages more generally. I'm really qualified to speak to just one of those. 

AUDIENCE: Hi, I've got two questions it's a bit earlier than what's supposed to be. So the first question is the packages that you're calling to use in the program, are they the same as, let's say, something Java the same as calling a class, a Java file in order to use its functions? 

And my second question is, what's the actual purpose of using command line arguments as you used because is not really the best way to, as you say, be user friendly where as in let's say the person who's using the program doesn't know what they want-- what the program's asking them? 

DAVID MALAN: Really good question. The first question about the comparison with Java, Python packages are similar to Java packages where you have something.something.something at the top of your program that gives you access to a class or something else. Python itself supports classes. More on those down the road. And you can do very similar things in Python as you can do with Java. But the analog really is Python packages to Java packages here. 

As for command line arguments, you ask a good question. Why do we use them, especially if they are literally user friendly? They're a little less user friendly to people who aren't in this Zoom to be honest. You and I as we learn more and more about programming and more about command line arguments, I daresay we'll become more comfortable with and tend to prefer the ability to customize commands using these command line arguments. Why? Productivity. It tends to make you faster because you get into the habit of knowing exactly how you can configure your software without having to manually answer questions. 

And case in point. All of this time have we been running Python of something.py. You could imagine not doing that. You can imagine typing only Python, hitting Enter. And then you're prompted for the name of the file you want to run. So you type in something.py, and then it runs. 

Not a big deal, but I would argue that over time, you're going to get a little tired of that TDM. And you would much prefer to just automate the command again and again and again, especially with little conveniences like being able to hit up and down in your keyboard history so as to rerun those same command. Automation is big too if you emerge from a class like this and start using Python to automate processes at work or for personal projects or the like, the ability to specify all of your inputs on the one line just means you can get work done more quickly. So hands down, absolutely. 

Using command line arguments is a more arcane feature of systems that most of us are no longer as familiar with because of Windows and Mac OS and other operating systems that have buttons and GUIs and menus. But the more comfortable you get with programming, I daresay the more you will tend to prefer these capabilities because they allow you to do things more quickly. 

With that said, allow me to propose that we take a turn toward, yet, another package that's particularly popular and just as easy to install all toward an end of using APIs. Now, APIs are not something that's Python-specific. More generally, an API is an application programming interface. And it can refer to Python files and functions. But often, APIs really refer to third-party services that you and I can write code that talk to. 

Many APIs, but not all, live on the internet these days so that so long as you have a browser or so long as you have some experience with Python programming or programming in any language, you can write code that in effect pretends to be a browser, connects to that third-party API on a server, and download some data that you can then incorporate into your own program. 

Now, how do you do this? Well, Python has a very popular package that you can install via pip called requests. The requests library allows you to make web request, internet request using Python code essentially as though you were a browser yourself. You can automate, therefore, the retrieval of URLs that start with HTTP or HTTPS. 

The documentation for this library is that a URL like this, but it too can be installed at the command line. And even though it's third party, it's one of the most popular and commonly used packages out there in Python. And this too is one of the reasons again that Python is so popular. There's just so many solutions to problems that you and I have or are invariably going to have when we write projects of our own. There's just a really vibrant ecosystem, a really vibrant community of open source software that's that easy for us to install. 

Let me go back to my terminal window now and run pip install requests in order to install this package on my own system. And after some lines of output, I'll see that it's successfully installed. Now, let's go ahead and create a new file here. For instance, itunes.py. It turns out that Apple has its own API for their iTunes service. The software that provides you with the ability to download and search for music and songs and other information as well. 

And it turns out that-- let me go back over to my computer here and open up a browser like Chrome. And let me go ahead and visit this URL here, https://itunes.apple.com/ search?entity=song&limit=1&term=weezer. Search?entity=song& limit=1&term=weezer. 

Now, I constructed this URL manually by reading the documentation for Apple's API-- application programming interface for iTune. And what they told me is that if I want to search for information about songs in their database, I should specify entity equals song so that songs and not albums or artists or something like that. If I just want to get back information on one song, I'm going to provide limit equals 1. And if the band I want to search for, the artist is Weezer, I should specify term equals Weezer. 

So with this, if I go ahead and hit Enter and visit this URL, I actually end up with a text file in my Downloads folder on my Mac. If I go ahead and open that text file that my browser just downloaded, we'll see all of this text here, which at first glance might look a bit cryptic, but it actually follows a pattern. 

Notice this curly brace at the start and notice this closed curly brace at the end. Notice this open square bracket here and notice this closed square bracket here. And in between those pieces of syntax are a whole bunch of strings and values. In fact, a whole bunch of key value pairs. What we're looking at here is a standard text format known as JSON-- JavaScript Object Notation, which yes, is technically related to yet, another programming language called JavaScript. But JSON itself is typically used nowadays as a language agnostic format for exchanging data between computers. 

By language agnostic, I mean you don't have to use JavaScript. You can use Python or any other language to read JSON or write it as well. And it's a completely text-based format, which means that if I visit that URL with my browser, what gets downloaded is just a bunch of text. 

But that text is formatted in a standard way using curly braces and square bracket using quotes and some colons that ultimately contains all of the information in Apple's database on Weezer's song, at least, the first one because I limited it to one in their database. And that's an API, an application programming interface. A mechanism whereby I can access data on someone else's server and somehow integrate it into my own program. 

Now, of course, my browser, Chrome, is not something I wrote. I should actually write some Python code that perhaps pretends to be a browser to grab this same data. So let's do that. Let me go back to VS Code here. And let me write a program with code, itunes.py. And we're going to write some code via which I can then use the iTunes API and in turn, Python to get information about any band that I might want. 

I'm going to go here and import first the requests library, which I installed earlier in order to make those HTTP requests. I'm going to go ahead and import the sys library via which I'll have the ability to use command line arguments like specification of the band that I want to search for if not Weezer. And then down here, I'm going to go ahead and insert some error checking to say if the length of sys.argv does not equal to-- so if the user does not provide me with the name of the file they want to run and the name of a band, and that's it, you know what. Let's just go ahead and exit for now. 

I could provide a more explanatory message. But for now, I'm going to keep things simple and just exit the program prematurely so that I can trust hereafter that sys.argv has what I want. And now, I have the opportunity to use the requests library to write some Python code that effectively is pretending to be a web browser so as to connect to that same HTTPS URL on Apple's own server. 

So now that I've guaranteed that the user has typed in not just the name of the file, but also the name of a band at the prompt giving me a length of two for sys.argv, let's go ahead and execute request stockget, which is a function inside of the request package that will literally get some response from a server. And the URL that I want to get is the exactly the same as before. https://itunes.apple.com/ search?entity=song& limit=1& term=previouslyweezer. 

But let's make this program a little interactive and actually allow the human to specify at the command line what artists they'd like to search for. So I'm going to go ahead and close my quote early and just append using the concatenation operator as in the past, sys.argv bracket1. 

And now, it actually be nice to store the response from the server in a variable. So I'm going to go ahead and say response equals and to store all of the response that comes back from the server in a variable called response. Down here now, I'd like to just understand what the server's returning to me to make sure I know how next to proceed. 

So this isn't going to be very pretty yet. But I'm going to go and print out response.json, which ensures that the data I'm getting back is formatted on my screen as exactly that, JSON, the same text format as we saw on my screen. It's not a useful program yet. I'm really just learning along the way. But let me go ahead now and increase the size of my terminal window and run Python of itunes.py and type in the name of a band like Weezer and hit Enter. 

And what we see on the screen formatted almost the same as before is exactly that same text. But what you'll see here is that this has been standardized now as a Python dictionary. What indeed Apple's returning is technically a JSON response, JavaScript Object Notation. But Python, the request library is converting it to a Python dictionary which happens to use wonderfully coincidentally, almost the same syntax. 

It uses curly braces to represent the dictionary here and a close curly brace to represent the end of it here. For any lists therein, it uses a square bracket here and a closed square bracket down here. It uses quotes-- single quotes in this case or equivalently double quotes to represent the keys in that dictionary. And after a colon, it stores the value of that key. 

And so you'll see that indeed we have a result count key whose value is 1, but then a more interesting Result key called results whose value is this entire list of data. Now, honestly, this is such a big blob of text that it's going to take me forever to wrap my mind around what I'm seeing. So let me propose temporarily we use another library in Python that will allow me to format my data a little more cleanly. 

It turns out that Python also comes with a special library called JSON that allows you to manipulate JSON data and even just printy print it that is formatted in a way that's going to be way easier for you and I to understand. So let me go back to my code here. Let me shrink my terminal window. And let me propose that just temporarily again we do this. 

Let me import this additional library, JSON, which comes with Python. So I don't need to install it manually with pip. And let me go ahead now and not just print out response.json which was that big blob of hard-to-understand text. Let me go ahead and use one other function here called json.dumps for dump string and pass to that function that response.json return value. 

So again, I'm just introducing another function who I claim has a purpose in life of pretty printing, nicely formatting on the screen the exact same information. And I know this from the documentation having done this before. But I'd like things to be nicely indented. And according to the documentation, if I pass in a named parameter of indent equals 2, that's going to indent everything at least two spaces. I could do four or something else. But it's going to be enough to help me wrap my mind around what the data is I'm getting back. Because again, I'm just learning along with you. 

So let me increase the size of my terminal window again. Let me run Python of itunes.py. And again, let's search for Weezer and hit Enter. And now, notice it's still a little bit cryptic because there's a lot going on here. But my gosh, I can totally read this more easily now. 

Notice now that I still see the first curly brace, which means hey, this is a dictionary in Python. A collection of keys and values. The first key is called result count. It happens to be displayed in double quotes now. But that's just an issue of formatting. It could be double or single so long as we're consistent. 

The value of that key is one. Why? Well, I told the URL to only limit the responses to one Weezer song so I've gotten a result set of one. If I increase that limit, I could probably get more. Then the interesting part of this response is really the data itself. Notice in the results key here, there's a really big value. The value is a Python list as implied by this square bracket. 

What does this list contain? Well, I know from skimming it earlier that this contains one dictionary. And that's why we see another curly brace here. So again, if this gets a little more complicated, keep in mind that a dictionary is just a collection of key value pairs. And Python uses curly braces to indicate as much. 

It is perfectly reasonable for a dictionary to be inside of another dictionary if the value of some key itself is another dictionary. So this is a common paradigm. And even though it might seem a bit cryptic, it's just something that allows us to associate more keys with more value. 

Now, most of this information, I probably don't care about. For instance, according to Apple, the unique identifier for Weezer is apparently 115,234. That might be useful if I'm making my own database and I want this to be searchable. But for today's purposes, all I care about is the name of the track, otherwise called track name as key. 

And the first song and only song because we limited it to one that we got back from iTunes here is the song that you might know by Weezer called Say It Ain't So. So now, I have a bit of a clue if my goal here is to implement a program called itunes.py that doesn't just dump the response from the server, which is admittedly very cryptic-- but to print out all of the songs that iTunes has for the band called Weezer, maybe I can iterate over this somehow. 

So let me backtrack. Here's the key call track name. It is inside of a dictionary that is the value of results here. So how can I go about getting this? Well, let me go ahead and try this. Let me go ahead and shrink my terminal window back down and let me propose now for one final flourish. We don't just lazily print out the contents of that response because that's not interesting or pretty for anyone. 

Let's do this. Let me go ahead and create a new variable just for the sake of discussion called O for object. And I'm going to go ahead and call o equals response.json just to store that JSON response specifically in a variable called o, but I could name it anything I want. And now, I'm going to do this. For each result in that object's key called results, go ahead and print out that result's track name. 

And notice I have used exactly the same capitalization. Track name has a capital N. Result is all lowercase. And let me rewind before we run the actual program. In line eight, we are making an HTTP request using Python to the server just like you and I as humans type URLs into a browser and hit Enter. This is the Python equivalent thereof. 

I am then on line 10 just grabbing from that variable that contains the server's response, the JSON object that I care about. The thing between those curly braces at the very top and the bottom. But because we've poked around and because I read the documentation earlier, I know that that object has a key called results. And that results key again is a list. 

Now, at the moment, that list contains only one song, Say It Ain't So, because I limited my response to one. But even so, my loop will work. It's just going to iterate once. And each time through that loop, it's going to print the current result's track name. 

If I want to make this even more interesting, let me change this limit now from 1 to 50 so I'll at least get back 50 track names instead. Let me go ahead now and increase the size of my terminal once more and go ahead now and run Python of itunes.py searching again for a band like Weezer. And here we go. And voila, there are 50 songs that iTunes has for Weezer. 

And if we scroll back up to the top here, we'll see that the very first one there is, indeed, Say It Ain't So. But now, we got Undone-- The Sweater Song, Buddy Holly. Apparently another rendition of Say It Ain't So perhaps from another album, another Buddy Holly undone, my name is Jonas, and so forth. Questions now on this program which integrates Python with a real world third party API? 

AUDIENCE: Yeah, hi. Can we use break instead of system.exit? 

DAVID MALAN: Good question, but no. Break again is used to break out of things like loops like we saw earlier. Sys.exit is used to break out of the whole program itself. Use break for loops for now and use sys.exit to terminate the whole program. Good question. Other questions now on this program are others? 

AUDIENCE: From where we bring the name of the key results? 

DAVID MALAN: From where do we get the name of the key? 

AUDIENCE: Results itself. Yeah, and can we change the results, the name? 

DAVID MALAN: You cannot. So we could in our program. So the keys that come back in that JSON response, to be clear, come from iTunes.Apple.com. Some team of engineers decided for us what all of those keys would be called, including track name, results, result count, and everything else. 

You and I can absolutely store those same values in variables just like I'm doing here with O, just like I'm doing here with result. You can rename those keys anything you want using Python variables. But the JSON response is coming from that third party server. Other questions. 

AUDIENCE: Yes, sir. So I have a question related to cowsay package. So like, yes. So sir, what sort of ASCII graphics is it capable of putting? 

DAVID MALAN: The cowsay package. I would refer you to the URL in the slides earlier if only because it's more thorough. They have not just cows, but Tyrannosaurus rex's and several other animals as well. I should emphasize that this is not a package I suspect you will use much in the real world. It's really just meant to be representative of the types of packages you can install. But allow me to refer to the documentation for what more is there. But ASCII art is all we had before there were emojis, let alone GIFs and JPEGs and pings. But it's what's is immortalized in cowsay. 

Well, allow me to transition us back now to one final capability of Python which is that you yourselves have the ability to make your own libraries. Up until now, we've been writing all of our functions in our one file, Hello py and everything since. And now that we've introduced modules in Python, random and statistics, we can import those that come with Python. But that's other people's code as well. 

And we've now used pip, this package manager to install third-party packages as well in the system and using other people's code still. But to come full circle, what if you yourself find yourself implementing the same kinds of functions again and again, or you find yourself opening up old programs, copying and pasting code you wrote into new programs because you have the same problem yet again? 

A good practice would be to somehow bundle up that code you keep reusing and make your own Python module or package. You can keep it local on your own Mac or PC or cloud server. Or you can go through the steps of actually bundling it up, making it free and open source, and putting it on something like py, pi for others to use as well? 

OK, I'm going to go ahead and run code of sayings.py to create a brand new file called sayings.py which is going to be my own sayings module. I'm going to define a couple of simple functions in there. I'm going to define a Hello function that's going to take a name parameter as input. And that function is simply going to print out an F string that contains hello, comma, and then in curly braces, whatever that person's name actually is. 

Then I'm going to go ahead and define one other function, a goodbye function, that has def, goodbye, also takes a name as its input. And then that prints out by contrast and F string that says goodbye, comma, and then in curly braces, name. And now, just for good measure just so I can be sure that these functions are working as expected, I'm going to go ahead and define a main function in here too just for the purposes of testing. 

And I'm going to go ahead and define a main function that simply does a couple of tests. For instance, it calls Hello of, quote, unquote, "world" shall we say? And then it's going to call good bye of, quote, unquote, "world" as well. And hopefully what I'll see on the screen then is Hello world and Goodbye world when I run this program. Of course, as always, I need to explicitly tell Python to call that function. So I'm going to call main at the very bottom of this file. 

All right, let's try it out. Python of sayings.py, Enter. And indeed, I see Hello world and Goodbye world. And so I think it's reasonable for me to assume that these functions, albeit simple, are pretty correct at this point. But now, suppose that I want to use these functions as though I've indeed created my own library, my own Python module and that makes available a Hello function for me or anyone else who wants to use it or a Goodbye function as well. 

Well, let me go ahead and open up again say.py but start fresh. And rather than have the cow say anything, let me go ahead and have my own library do the talking. So I'm going to go ahead and as before, import sys so that I have access to command line arguments. And from my own module called sayings, I'm going to import Hello. 

So because I created a file called sayings.py, I can say from sayings. And it's inferred by Python that I mean sayings.py, at least in this current directory. But I specifically ain't going to import just one of the functions for now, namely Hello. 

And now, I can do something like this. If the user obliges by giving me two command line arguments, which I can check by just checking the length of sys.argv, I'm going to then go ahead and call this new Hello function passing as its input, sys.argvbracket1, which should hopefully be the person's name which I'm going to expect them to type at the prompt. 

So here we go. I'm going to go down to my terminal window, run Python of say.py and my own name because I want my own name to end up in the command line arguments and therefore, be part of the Hello so when I hit Enter in just a moment, I should hopefully see Hello, comma, David. 

So here we go, Enter. And huh, I see Hello world, Goodbye world. And then I see Hello, David. So why is this happening? Well, it turns out even though I've done everything according to our own past practice, it's not really the right way to go about calling main after all. If I'm blindly calling main here at the bottom of my file, that means whenever this file is loaded by Python, main is going to get called. 

And unfortunately, that's true even if I'm importing this file or just a function from this file as I am here in my say.py program. This is to say on line three here, when I say from sayings, import Hello, this effectively tells Python to go find that module, sayings.py, read it from top to bottom, left to right, and then import specifically the Hello function. 

Unfortunately by the time Python has read the file from top to bottom, left to right, that last line of code recall is to call main. Main gets called no matter what. So really, the right way to go about using a main function, which does solve that problem of ensuring that we can order our functions however we want, and all the functions will be defined at the time they're invoked, I shouldn't be unconditionally calling main at the bottom of this or really any of my programs. 

I should instead use this technique. I should say if__name__=="__main__", then and only then should you actually call main. Well, it turns out that this variable is a special symbol in Python, __name__. And notice that VS Code because of its font isn't quite showing those two underscores. But they're indeed there to the left and the right. 

This is a special variable whose value is automatically set by Python to be, quote, unquote, "main" when you run a file from the command line as by running Python of sayings.py. So watch what happens now with this additional conditional in sayings.py. If I run Python of sayings.py, it still works as before because name will be automatically set to __main__ when I run this file using Python of sayings.py. 

But notice this. Name is not going to be set to, quote, unquote, "main." It's going to be set to something else, technically the name of the module when I instead import the file like I do here. So this highlighted line of code even though it will cause Python to go find sayings.py, read it from top to bottom, left to right, it's going to ignore the call to main this time because it's wrapped in that conditional. 

In this case, when I'm importing a file and not running it directly at the command line, main will not get called by definition of that names value. So let me go ahead and try this. Instead of running Python of sayings.py, which is the module, which contains that conditional main, let me go ahead here, run Python of say.py, which is the program here before me that imports Hello from sayings. But because of that conditional, it's not going to say Hello to anyone else except me in this case. 

All right, we're here at the end of our week. It's only appropriate, I think, to import something other than Hello. Why don't I go ahead and import not Hello, but Goodbye from here. Let me go ahead and call Goodbye instead of Hello. And this time when I run Python of say.py, I'm not going to type my own name. Allow me if I may to type in the whole world so that our final sentiment today is Goodbye world. Indeed, that's it for this week. We will see you next time. 
"""
