# CS50's Introduction to Programming with Python (CS50P) 2022 
# https://cs50.harvard.edu/python/2022/weeks/5/
# https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V
# https://youtu.be/tIrcxwLqzjQ

# https://cs50.harvard.edu/python/2022/notes/5/

# RECOMEÇANDO! 2023-08-03

print("Hello, world!")
print("Hello, world!")
print("Hello, world!")

"""
Lecture 5 - Unit Tests
  assert
  pytest
  Testing Strings
  Organizing Tests into Folders
  Summing Up
"""

"""
Unit Tests
Up until now, you have been likely testing your own code using print statements.
Alternatively, you may have been relying upon CS50 to test your code for you!
It’s most common in industry to write code to test your own programs.
In your console window, type code calculator.py. Note that you may have previously coded this file in a previous lecture. In the text editor, make sure that your code appears as follows:
"""
def main ():
  x = int(input("What's x? "))
  print("x squared is", square(x))


def square(n):
  return n * n


if __name__ == "__main__":
  main()
"""
Notice that you could plausibly test the above code on your own using some obvious numbers such as 2. However, consider why you might want to create a test that ensures that the above code functions appropriately.
Following convention, let’s create a new test program by typing code test_calculator.py and modify your code in the text editor as follows:
"""
