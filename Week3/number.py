x = int(input("What's x? "))
print(f"The value of x is {x}.")



# VALUE ERROR

"""
>>> x = int(input("What's x? "))
What's x? 10

>>> x = int(input("What's x? "))
What's x? cat

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'cat'
"""



# TRY - here we catch the error ValueError and return a message saying it is not an integer when we type 'cat'. 

try: 
    x = int(input("What's x? "))
    print(f"The value of x is {x}.")
except ValueError:
    print("We have a ValueError, for x is not an INTeger.")

try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")

print(f"x is {x}") # The idea is to reduce "try" to minimun lines of code, so we keep the output outside of the scope...

# NAME ERROR - So if we take out the print() we should receive the message of the except catched by the ValueError...

try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")

# We find ourselves in a new NameError: x is not defined. 

"""
X is not defined, even thou we have written it. The idea behind it is that when we prompt the user for a string (input) converted to an int int() we should expect a number.
When the user types something different of a number, hits enter, or put 'cat' into the prompt, the syntax will be truked and an error will occur "ValueError" and as an exception situation, the function WILL NOT ASSIGN TO X anything.
Without an assignment to X of an integer, X is not defined, creating another problem of NameError. 
"""

try:
    x = int(input("What's x?"))
except ValueError: # Here we catch the error and terminate the program.
    print("x is not an integer")
else: # If we try x and there are no problems caught before (like 'cat'), then we end with an else case printing the value of x. 
    print(f"x is {x}")

# What if the user types anything wrong, the code simple terminates? No good idea, let's use an infinity loop to "gently" remember the user what we want (without being explicit).

# WHILE TRUE

while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")



### CREATING A FUNCTION TO GET AN INTEGER

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()

# Notice that we are manifesting many great properties. First, we have abstracted away the ability to get an integer. Now, this whole program boils down to the first three lines of the program.
# Even still, we can improve this program. Consider what else you could do to improve this program. Modify your code as follows:

def main():
    x = get_int()
    print(f"x is {x}")


def get_int(n):
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x # same as break

main()

# Notice that return will not only break you out of a loop, but it will also return a value.
# Some people may argue you could do the following:

def main():
    x = get_int()
    print(f"x is {x}")


def get_int(n):
    while True:
        try:
            return int(input("What's x? ")) # look the return statment here... it returns and breaks...
        except ValueError:
            print("x is not an integer")

main()



# PASS

# We can make it such that our code does not warn our user, but simply re-asks them our prompting question by modifying our code as follows:
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass


main()
# Notice that our code will still function but will not repeatedly inform the user of their error. In some cases, you’ll want to be very clear to the user what error is being produced. Other times, you might decide that you simply want to ask them for input again.

# PASS + prompt

# One final refinement that could improve the implementation of this get_int function. Right now, notice that we are relying currently upon the honor system that the x is in both the main and get_int functions. We probably want to pass in a prompt that the user sees when asked for input. Modify your code as follows.

def main():
    x = get_int("What's x? ")
    print(f"The value of x is {x}.")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()

""" 
ABOUT THE PASS AND PROMPT
Well, let me propose some final refinements to this program that really just kind of tighten things up, one additional step to improve the implementation of this get int function. Let me propose that we not hard code, so to speak-- that is type manually x all over the place. Let's make this function, get int, a little more reusable. 
Right now, notice that I'm just kind of using the honor system that, well, main is defining a variable called x. And get int is asking for a variable called x. But it would be nice if the caller, main, doesn't have to know what the call-ee is naming its variables and vise versa. So caller-- to call a function means to use it. The caller is the function that's using it. 
The call-ee is just the function being called. It would be nice if I'm not just hoping that x is the same in both places. So let me propose this. Let me propose that we actually add a parameter to get int, like this. What's x? 
That is to say, if main wants to use the get int function, well, then main should probably tell the get int function what prompt to show the user. Just like the input function, recall, that comes with Python, it's up to you to pass in a prompt that the user then sees when the human is asked for input. So how do I make this work here? 
I can go down to my definition of get int. And I can say, all right, get int is going to take a parameter now, called prompt. I could call it anything I want. But prompt in English is pretty self-explanatory. 
It means the message the user will see. And now, down here, when I actually use input, I don't have to presumptuously say, what's x? Because what if the program, the caller, wants to ask for y or z or some other variable? I can just pass to input whatever prompt the caller has provided. 
So now I'm making more reusable code. It still works just the same. I haven't changed the functionality, per se. But now it's a little more dynamic because now get int doesn't have to know or care what variable's being asked for, what's being asked for. It just needs to know what prompt it should show to the user. 
So if I now run this program down here, again, prompt number.py, Enter, what's x? 50 still seems to work. Let's run it again. Let's type in cat. 
It still seems to work. And if I type in cat, dog, bird, or anything else, it will keep prompting me with that same prompt, making this code, therefore, all the more usable. Now it turns out, too, you can even raise exceptions yourself using Python's raise keyword. But more on that another time. 
"""