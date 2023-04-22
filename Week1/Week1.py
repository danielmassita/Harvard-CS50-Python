# CS50's Introduction to Programming with Python (CS50P) 2022 
# https://cs50.harvard.edu/python/2022/weeks/1/
# https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V
# https://youtu.be/_b6NgY_pMdw

"""
Conditionals
Conditionals allow you, the programmer, to allow your program to make decisions: As if your program has the choice between taking the left-hand road or the right-hand road based upon certain conditions.
Built within Python are a set of “operators” that can are used to ask mathematical questions.
> and < symbols are probably quite familiar to you.
>= denotes “greater than or equal to.”
<= denotes “less than or equal to.”
== denotes “equals, though do notice the double equal sign! A single equal sign would assign a value. Double equal signs are used to compare variables.
!= denotes “not equal to.
Conditional statements compare a left-hand term to a right-hand term.

if Statements
In your terminal window, type code compare.py. This will create a brand new file called “compare.”
In the text editor window, begin with the following:

    x = int(input("What's x? "))
    y = int(input("What's y? "))

    if x < y:
        print("x is less than y")
    Notice how your program takes the input of the user for both x and y, casting them as integers and saving them into their respective x and y variables. Then, the if statement compares x and y. If the condition of x < y is met, the print statement is executed.

If statements use bool or boolean values (true or false) to decide whether or not to execute. If the statement of x > y is true, the compiler will register it as true and execute the code.



Control Flow, elif, and else
Further revise your code as follows:

    x = int(input("What's x? "))
    y = int(input("What's y? "))

    if x < y:
        print("x is less than y")
    if x > y:
        print("x is greater than y")
    if x == y:
        print("x is equal to y")
    Notice how you are providing a series of if statements. First, the first if statement is evaluated. Then, the second if statement runs its evaluation. Finally, the last if statement runs its evaluation. This flow of decisions is called “control flow.”

Our code can be represented as follows:

# Image1 - 

This program can be improved by not asking three consecutive questions. After all, not all three questions can have an outcome of true! Revise your program as follows:

    x = int(input("What's x? "))
    y = int(input("What's y? "))

    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    elif x == y:
        print("x is equal to y")
    Notice how the use of elif allows the program to make less decisions. First, the if statement is evaluated. If this statement is found to be true, all the elif statements not be run at all. However, if the if statement is evaluated and found to be false, the first elif will be evaluated. If this is true, it will not run the final evaluation.

Our code can be represented as follows:

# Image2 - 

While your computer may not notice a difference speed-wise between our first program and this revised program, consider how an online server running billions or trillions of these types of calculations each day could definitely be impacted by such a small coding decision.
There is one final improvement we can make to our program. Notice how logically elif x == y is not a necessary evaluation to run. After all, if logically x is not less than y AND x is not greater than y, x MUST equal y. Therefore, we don’t have to run elif x == y. We can create a “catch-all,” default outcome using an else statement. We can revise as follows:

    x = int(input("What's x? "))
    y = int(input("What's y? "))

    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print("x is equal to y")
    Notice how the relative complexity of this program has decreased through our revision.

Our code can be represented as follows:

# Image3 - 

or
or allows your program to decide between one or more alternatives. For example, we could further edit our program as follows:

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
Notice that the result of our program is the same, but the complexity is decreased and the efficiency of our code is increased.

At this point, our code is pretty great. However, could the design be further improved? We could further edit our code as follows:

x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
Notice how we removed the or entirely, and simply asked “is x not equal to y?” We ask one and only one question. Very efficient!

For the purpose of illustration, we could also change our code as follows:

x = int(input("What's x? "))
y = int(input("What's y? "))

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")
Notice that the == operator evaluates if what is on the left and right are equal to one another. That use of double equal signs is very important. If you use only one equal sign, an error will likely be thrown by the compiler.

Our code can be illustrated as follows:

True
False
start
x == y
"x is equal to y"
"x is not equal to y"
stop
and
Similar to or, and can be used within conditional statements.
Execute in the terminal window code grade.py. Start your new program as follows:

score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >=80 and score < 90:
    print("Grade: B")
elif score >=70 and score < 80:
    print("Grade: C")
elif score >=60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")
Notice that executing python grade.py you will be able to input a score and get a grade. However, notice how there are potentials for bugs.

Typically, we do not want to ever trust our user to input the correct information. We could improve our code as follows:

  score = int(input("Score: "))

  if 90 <= score <= 100:
      print("Grade: A")
  elif 80 <= score < 90:
      print("Grade: B")
  elif 70 <= score < 80:
      print("Grade: C")
  elif 60 <= score < 70:
      print("Grade: D")
  else:
      print("Grade: F")
Notice how Python allows you to chain together the operators and conditions in a way quite uncommon to other programming languages.

Still, we can further improve our program:

score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
Notice how the program is improved by asking fewer questions. This makes our program easier to read and far more maintainable in the future.

You can learn more in Python’s documentation on control flow.

"""
