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