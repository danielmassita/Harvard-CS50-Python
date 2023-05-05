# CS50's Introduction to Programming with Python (CS50P) 2022 
# https://cs50.harvard.edu/python/2022/weeks/2/
# https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V
# https://youtu.be/-7xg8pGcP6w

# https://cs50.harvard.edu/python/2022/notes/2/

"""
Lecture 2
Loops
While Loops
For Loops
Improving with User Input
More About Lists
Length
Dictionaries
Mario
Summing Up
"""

"""
Loops
Essentially, loops are a way to do something over and over again.
Begin by typing code cat.py in the terminal window.
In the text editor, begin with the following code:

    print("meow")
    print("meow")
    print("meow")
    
Running this code by typing python cat.py, you’ll notice that the program meows three times.

In developing as a programmer, you want to consider how one could improve areas of one’s code where one types the same thing over and over again. Imagine where one might want to “meow” 500 times. Would it be logical to type that same expression of print("meow") over and over again?
Loops enable you to create a block of code that executes over and over again.
"""



"""
While Loops
The while loop is nearly universal throughout all coding languages.
Such a loop will repeat a block of code over and over again.
In the text editor window, edit your code as follows:

i = 3
while i != 0:
    print("meow")
Notice how even though this code will execute print("meow") multiple times, it will never stop! It will loop forever. while loops work by repeatedly asking if the condition of the loop has been fulfilled. In this case, the compiler is asking “does i not equal zero?” When you get stuck in a loop that executes forever, you can press control-c on your keyboard to break out of the loop.

To fix this loop that lasts forever, we can edit our code as follows

i = 3
while i != 0:
  print("meow")
  i = i - 1
Notice that now our code executes properly, reducing i by 1 for each “iteration” through the loop. This term iteration has special significance within coding. By iteration, we mean one cycle through the loop. The first iteration is the “0th” iteration through the loop. The second is the “1st” iteration. In programming we count starting with 0, then 1, then 2.

We can further improve our code as follows:

  i = 1
  while i <= 3:
      print("meow")
      i = i + 1
Notice that when we code i = i + 1 we assign the value of i from the right to the left. Above, we are starting i at one, like most humans count (1, 2, 3). If you execute the code above, you’ll see it meows three times. It’s best practice in programming to begin counting with zero.

We can improve our code, to start counting with zero:

i = 0
while i < 3:
    print("meow")
    i += 1
Notice how changing the operator to i < 3 allows our code to function as intended. We begin by counting with 0 and it iterates through our loop three times, producing three meows. Also, notice how i += 1 is the same as saying i = i + 1.

Our code at this point is illustrated as follows:
<image>
Notice how our loop counts i up to, but not through 3.
"""



"""
For Loops
A for loop is a different type of loop.
To best understand a for loop, it’s best to begin by talking about a new variable type called a list in Python. As in other areas of our lives, we can have a grocery list, a to-do list, etc.
A for loop iterates through a list of items. For example, in the text editor window, modify your cat.py code as follows:

for i in [0, 1, 2]:
    print("meow")
Notice how clean this code is compared to your previous while loop code. In this code, i begins with 0, meows, i is assigned 1, meows, and, finally, i is assigned 2, meows, and then ends.

While this code accomplishes what we want, there are some possibilities for improving our code for extreme cases. At first glance, our code looks great. However, what if you wanted to iterate up to a million? It’s best to create code that can work with such extreme cases. Accordingly, we can improve our code as follows:

for i in range(3):
    print("meow")
Notice how range(3) provides back three values (0, 1, and 2) automatically. This code will execute and produce the intended effect, meowing three times.

Our code can be further improved. Notice how we never use i explicitly in our code. That is, while Python needs the i as a place to store the number of the iteration of the loop, we never use it for any other purpose. In Python, if such a variable does not have any other significance in our code, we can simply represent this variable as a single underscore _. Therefore, you can modify your code as follows:

for _ in range(3):
    print("meow")
Notice how changing the i to _ has zero impact on the functioning of our program.

Our code can be further improved. To stretch your mind to the possibilities within Python, consider the following code:

print("meow" * 3)
Notice how it will meow three times, but the program will produce meowmeowmeow as the result. Consider: How could you create a line break at the end of each meow?

Indeed, you can edit your code as follows:

print("meow\n" * 3, end="")
Notice how this code produces three meows, each on a separate line. By adding end="" and the \n we tell the compiler to add a line break at the end of each meow.
"""