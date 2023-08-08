# CS50's Introduction to Programming with Python (CS50P) 2022 
# https://cs50.harvard.edu/python/2022/weeks/5/
# https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V
# https://youtu.be/tIrcxwLqzjQ

# https://cs50.harvard.edu/python/2022/notes/5/

# RECOMEÇANDO! 2023-08-03

"""
Lecture 5 - Unit Tests
  assert
  pytest
  Testing Strings
  Organizing Tests into Folders
  Summing Up
"""

"""
UNIT TESTS

- Up until now, you have been likely testing your own code using print statements.
- Alternatively, you may have been relying upon CS50 to test your code for you!
- It’s most common in industry to write code to test your own programs.
- In your console window, type code calculator.py. Note that you may have previously coded this file in a previous lecture. In the text editor, make sure that your code appears as follows:
"""
def main ():
  x = int(input("What's x? "))
  print("x squared is", square(x))


def square(n):
  return n * n


if __name__ == "__main__":
  main()
"""
- Notice that you could plausibly test the above code on your own using some obvious numbers such as 2. However, consider why you might want to create a test that ensures that the above code functions appropriately.
- Following convention, let’s create a new test program by typing code test_calculator.py and modify your code in the text editor as follows:
"""
from calculator import square


def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")


if __name__ == "__main__":
    main()
"""
- Notice that we are importing the square function from square.py on the first line of code. By convention, we are creating a function called test_square. Inside that function, we define some conditions to test.
- In the console window, type python test_calculator.py. You’ll notice that nothing is being outputted. It could be that everything is running fine! Alternatively, it could be that our test function did not discover one of the “corner cases” that could produce an error.
- Right now, our code tests two conditions. If we wanted to test many more conditions, our test code could easily become bloated. How could we expand our test capabilities without expanding our test code?
- Luckly, I only see one error, because by chance, 2 squared with 2+2 indeed equals 4.

ASSERT

- Python’s assert command allows us to tell the compiler that something, some assertion, is true. We can apply this to our test code as follows:
"""
from calculator import square


def main():
    test_square()


def test_square():
    assert square(2) == 4
    assert square(3) == 9


if __name__ == "__main__":
    main()
"""
- Notice that we are definitively asserting what square(2) and square(3) should equal. Our code is reduced from four test lines down to two.
- We can purposely break our calculator code by modifying it as follows:
"""
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n + n


if __name__ == "__main__":
    main()
"""
- Notice that we have changed the * operator to a + in the square function.
- Now running python test_square.py in the console window, you will notice that an AssertionError is raised by the compiler. Essentially, this is the compiler telling us that one of our conditions was not met.
- One of the challenges that we are now facing is that our code could become even more burdensome if we wanted to provide more descriptive error output to our users. Plausibly, we could code as follows:
"""
from calculator import square


def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared is not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared is not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared is not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared is not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared is not 0")


if __name__ == "__main__":
    main()
"""
- Notice that running this code will produce multiple errors. However, it’s not producing all the errors above. This is a good illustration that it’s worth testing multiple cases such that you might catch situations where there are coding mistakes.

- The above code illustrates a major challenge: How could we make it easier to test your code without dozens of lines of code like the above?
- You can learn more in Python’s documentation of assert.
- https://docs.python.org/3/reference/simple_stmts.html#assert
"""
