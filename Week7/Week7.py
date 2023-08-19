# CS50's Introduction to Programming with Python (CS50P) 2022 
# https://cs50.harvard.edu/python/2022/weeks/7/
# https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V
# https://www.youtube.com/watch?v=hy3sd9MOAcc

# https://cs50.harvard.edu/python/2022/notes/7/

"""
Lecture 7
    
    Regular Expressions
    Case Sensitivity
    Cleaning Up User Input
    Extracting User Input
    Summing Up
"""

# REGULAR EXPRESSIONS

# Regular expressions or “regexes” will enable us to examine patterns within our code. For example, we might want to validate that an email address is formatted correctly. Regular expressions will enable us to examine expressions in this fashion.

# To begin, type code validate.py in the terminal window. Then, code as follows in the text editor:

email = input("What's your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")

# Notice that strip will remove whitespace at the beginning or end of the input. Running this program, you will see that as long as an @ symbol is inputted, the program will regard the input as valid.

# You can imagine, however, that one could input @@ alone and the input could be regarded as valid. We could regard an email address as having at least one @ and a . somewhere within it. Modify your code as follows:

email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")

