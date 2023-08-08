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

  ```
  Harvard-CS50p/Week5/ $ python test_calculator.py
  3 squared was not 9
  -2 squared was not 4
  -3 squared was not 9
  Harvard-CS50p/Week5/ $ 
  ```

- Notice that running this code will produce multiple errors. However, it’s not producing all the errors above. This is a good illustration that it’s worth testing multiple cases such that you might catch situations where there are coding mistakes.

- The above code illustrates a major challenge: How could we make it easier to test your code without dozens of lines of code like the above?
- You can learn more in Python’s documentation of assert.
- https://docs.python.org/3/reference/simple_stmts.html#assert

PYTEST

- pytest is a third-party library that allows you to unit test your program. That is, you can test your functions within your program.
- To utilize pytest please type pip install pytest into your console window.
- Before applying pytest to our own program, modify your test_calculator function as follows:
"""
from calculator import square


def test_assert():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

    """
    rootdir: /workspaces/111195175/Harvard-CS50p/Week5
    collected 1 item                                                                                                         
    
    test_calculator.py F                                                                                               [100%]
    
    ======================================================== FAILURES ========================================================
    ______________________________________________________ test_square _______________________________________________________
    
        def test_square():
            assert square(2) == 4
    >       assert square(3) == 9
    E       assert 6 == 9
    E        +  where 6 = square(3)                   <<<<< MAYBE THE ERROR SHOULD BE SOMEWHERE OVER HERE...
    
    test_calculator.py:46: AssertionError
    ================================================ short test summary info =================================================
    FAILED test_calculator.py::test_square - assert 6 == 9
    =================================================== 1 failed in 0.15s ====================================================
    Harvard-CS50p/Week5/ $ pytest test_calculator.py
    """
"""
- Notice how the above code asserts all the conditions that we want to test.
- pytest allows us to run our program directly through it, such that we can more easily view the results of our test conditions.
- In the terminal window, type pytest test_calculator.py. You’ll immediately notice that output will be provided. Notice the red F near the top of the output, indicating that something in your code failed. Further, notice that the red E provides some hints about the errors in your calculator.py program. Based upon the output, you can imagine a scenario where 3 * 3 has outputted 6 instead of 9. Based on the results of this test, we can go correct our calculator.py code as follows:
"""
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
"""
- Notice that we have changed the + operator to a * in the square function, returning it to a working state.
- Re-running pytest test_calculator.py, notice how no errors are produced. Congratulations!
- At the moment, it is not ideal that pytest will stop running after the first failed test. Again, let’s return our calculator.py code back to its broken state:
"""
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n + n


if __name__ == "__main__":
    main()
"""
- Notice that we have changed the * operator to a + in the square function, returning it to a broken state.
- To improve our test code, let’s modify test_calculator.py to divide the code into different groups of tests:
"""
from calculator import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0

"""
Harvard-CS50p/Week5/ $ pytest test_calculator.py
================================================== test session starts ===================================================
platform linux -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0
rootdir: /workspaces/111195175/Harvard-CS50p/Week5
collected 3 items                                                                                                        

test_calculator.py FF.                                                                                             [100%]

======================================================== FAILURES ========================================================
_____________________________________________________ test_positive ______________________________________________________

    def test_positive():
        assert square(2) == 4
>       assert square(3) == 9
E       assert 6 == 9
E        +  where 6 = square(3)

test_calculator.py:57: AssertionError
_____________________________________________________ test_negative ______________________________________________________

    def test_negative():
>       assert square(-2) == 4
E       assert -4 == 4
E        +  where -4 = square(-2)

test_calculator.py:60: AssertionError
================================================ short test summary info =================================================
FAILED test_calculator.py::test_positive - assert 6 == 9
FAILED test_calculator.py::test_negative - assert -4 == 4
============================================== 2 failed, 1 passed in 0.07s ===============================================
Harvard-CS50p/Week5/ $ 
"""

"""
- Notice that we have divided the same five tests into three different functions. Testing frameworks like pytest will run each function, even if there was a failure in one of them. Re-running pytest test_calculator.py, you will notice that many more errors are being displayed. More error output allows you to further explore what might be producing the problems within your code.
- Having improved our test code, return your calculator.py code to fully working order:
"""
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
"""

    ```
    Harvard-CS50p/Week5/ $ pytest test_calculator.py
    ================================================== test session starts ===================================================
    platform linux -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0
    rootdir: /workspaces/111195175/Harvard-CS50p/Week5
    collected 3 items                                                                                                        
    
    test_calculator.py ...                                                                                             [100%]
    
    =================================================== 3 passed in 0.01s ====================================================
    Harvard-CS50p/Week5/ $ 
    ```


- Notice that we have changed the + operator to a * in the square function, returning it to a working state.
- Re-running pytest test_calculator.py, you will notice that no errors are found.
- In summary, it’s up to you as a coder to define as many test conditions as you see fit!
- You can learn more in Pytest’s documentation of pytest.
- https://docs.pytest.org/en/7.1.x/getting-started.html


TESTING STRINGS

- Going back in time, consider the following code hello.py:
"""
def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


if __name__ == "__main__":
    main()
"""
- Notice that we may wish to test the result of the hello function.
- Consider the following code for test_hello.py:
"""
