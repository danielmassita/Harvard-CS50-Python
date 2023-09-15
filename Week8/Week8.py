# CS50's Introduction to Programming with Python (CS50P) 2022 
# https://cs50.harvard.edu/python/2022/weeks/8/
# https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V
# https://youtu.be/e4fwY9ZsxPw

# https://cs50.harvard.edu/python/2022/notes/8/

"""
Lecture 8
    Object-Oriented Programming
    Classes
    raise
    Decorators
    Connecting to Previous Work in this Course
    Class Methods
    Static Methods
    Inheritance
    Inheritance and Exceptions
    Operator Overloading
    Summing Up
"""





"""
Object-Oriented Programming

- There are different paradigms of programming. As you learn other languages, you will start recognizing patterns like these.
- Up until this point, you have worked procedurally step-by-step.
- Object-oriented programming (OOP) is a compelling solution to programming-related problems.
- To begin, type code student.py in the terminal window and code as follows:
"""
    name = input("Name: ")
    house = input("House: ")
    print(f"{name} from {house}")
"""
- Notice that this program follows a procedural, step-by-step paradigm: Much like you have seen in prior parts of this course.
- Drawing on our work from previous weeks, we can create functions to abstract away parts of this program.
"""
    def main():
        name = get_name()
        house = get_house()
        print(f"{name} from {house}")
    
    def get_name():
        return input("Name: ")
    
    def get_house():
        return input("House: ")
        
    if __name__ == "__main__":
        main()
"""
- Notice how get_name and get_house abstract away some of the needs of our main function. Further, notice how the final lines of the code above tell the compiler to run the main function.
- We can further simplify our program by storing the student as a tuple. A tuple is a sequences of values. Unlike a list, a tuple can’t be modified. In spirit, we are returning two values.
"""


# https://youtu.be/e4fwY9ZsxPw?si=D-XQhsI-7IrBdRCf&t=7401
