# CS50's Introduction to Programming with Python (CS50P) 2022 
# https://cs50.harvard.edu/python/2022/weeks/8/
# https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V
# https://youtu.be/e4fwY9ZsxPw

# https://cs50.harvard.edu/python/2022/notes/8/

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

def main():
    name, house = get_student() # unpack technique
    print(f"{name} from {house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house # returns a Tuple


if __name__ == "__main__":
    main()

"""
- Notice how get_student returns name, house.
- Packing that tuple, such that we are able to return both items to a variable called student, we can modify our code as follows.
"""

def main():
    student = get_student() # single variable receiving a tuple
#    print(f"{name} from {house}") # will raise a NameError (not assigned variable)
    print(f"{student[0]} from {student[1]}") # we use index[0] for name and index[1] for house

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) # (variable1, variable2) in a (Tuple) type


if __name__ == "__main__":
    main()

"""
- Notice that (name, house) explicitly tells anyone reading our code that we are returning two values within one. Further, notice how we can index into tuples using student[0] or student[1].
- tuples are immutable, meaning we cannot change those values. Immutability is a way by which we can program defensively.
"""

def main():
    student = get_student()

    if student[0] == "Padma": # this index student[0] reads 'Padma' from name
        student[1] = "Ravenclaw" # and converts the index student[1] into 'Ravenclaw' even the user typed something else

    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) # Will raise an TypeError for Tuples are immutables


if __name__ == "__main__":
    main()

"""
- Notice that this code produces an error. Since tuples are immutable, we’re not able to reassign the value of student[1].
- If we wanted to provide our fellow programmers flexibility, we could utilize a list as follows.
"""

def main():
    student = get_student()

    if student[0] == "Padma":
        student[1] = "Ravenclaw" # Tuples are immutable and Lists are mutables!

    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house] # returns a List!


if __name__ == "__main__":
    main()

"""
- Note the lists are mutable. That is, the order of house and name can be switched by a programmer. You might decide to utilize this in some cases where you want to provide more flexibility at the cost of the security of your code. After all, if the order of those values is changeable, programmers that work with you could make mistakes down the road.
- A dictionary could also be utilized in this implementation. Recall that dictionaries provide a key-value pair.
"""

def main():
    student = get_student()
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}") # access the keys 'name' and 'house' but NOT DOUBLE QUOTES because of the f-string


def get_student():
    student = {} # Starts an empty Dict
    student["name"] = input("Name: ") # index[0] is now the KEY 'name'
    student["house"] = input("House: ") # index[1] is now the KEY 'house'
    return student # wich will be a Dict type from line 130.


if __name__ == "__main__":
    main()

"""
- Notice in this case, two key-value pairs are returned. An advantage of this approach is that we can index into this dictionary using the keys.
- Still, our code can be further improved. Notice that there is an unneeded variable. We can remove student = {} because we don’t need to create an empty dictionary.
"""

def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house} # Readability for keys 'name' and 'house'. Not use if TOO LONG coding lines...


if __name__ == "__main__":
    main()

"""
- Notice we can utilize {} braces in the return statement to create the dictionary and return it all in the same line.
- We can provide our special case with Padma in our dictionary version of our code.
"""

def main():
    student = get_student()
    if student['name'] == "Padma":
        student['house'] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house} # DICTs are mutables!


if __name__ == "__main__":
    main()

"""
- Notice how, similar in spirit to our previous iterations of this code, we can utilize the key names to index into our student dictionary.


Classes

- Classes are a way by which, in object-oriented programming, we can create our own type of data and give them names.
- A class is like a mold for a type of data – where we can invent our own data type and give them a name.
- We can modify our code as follows to implement our own class called Student:
"""

class Student:
    ...

def main():
    student = get_student()
    # if student["name"] == "Padma":
    #     student["house"] = "Ravenclaw"
    # print(f"{student['name']} from {student['house']}")
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student() # Calling a function to "class Student", to create an OBJECT of that CLASS (blueprint, mold)
    # When assinging a OBJECT from a CLASS we are INSTANTIATING (instances)
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()

"""
- Notice by convention that Student is capitalized. Further, notice the ... simply means that we will later return to finish that portion of our code. Further, notice that in get_student, we can create a student of class Student using the syntax student = Student(). Further, notice that we utilize “dot notation” to access attributes of this variable student of class Student.
- Any time you create a class and you utilize that blueprint to create something, you create what is called an “object” or an “instance”. In the case of our code, student is an object.
- Further, we can lay some groundwork for the attributes that are expected inside an object whose class is Student. We can modify our code as follows:
"""

class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house) # We receive input from user, storing in local variables, calling Student() passing (name, house) as ARGUMENTS
    # We can have more CONTROL over the correcteness of the data
    return student


if __name__ == "__main__":
    main()

"""
- There are a number of not just attributes or instance variables that you can put inside, but also METHODS.
- Classes come with certain methods, or functions inside of them, that you can define, and they just behave in a special way, by nature of how Python works.
- These functions allow you to determine behavior in a standard way.
- They are special methods in that sense.
"""

class Student:
    def __init__(self, name, house): # Dunder INIT method is an instance method - INITIALIZE THE CONTENT OF THIS OBJECT FROM A CLASS
        self.name = name # parameter self.name
        self.house = house # parameter self.house
        # we're adding variables to objects, aka INSTANCE VARIABLES TO OBJECTS
        # Installing into the "empty object" the values of name, house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():

    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house) # CONSTRUCTOR CALL
    # construct a student object for me || Insanciate a student object for me || Using class as a MOLD to work with arguments (self, name, house)
    # Can pass Student(arguments, arguments) to customize the content of that object.
    # We call the function that was defined with __init__(self, name, house)
    return student


if __name__ == "__main__":
    main()

"""
- Notice that within Student, we standardize the attributes of this class. We can create a function within class Student, called a “method”, that determines the behavior of an object of class Student. Within this function, it takes the name and house passed to it and assigns these variables to this object. Further, notice how the constructor student = Student(name, house) calls this function within the Student class and creates a student. self refers to the current object that was just created.
- We can simplify our code as follows:
"""

# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)


# if __name__ == "__main__":
#     main()

"""
- Notice how return Student(name, house) simplifies the previous iteration of our code where the constructor statement was run on its own line.
- You can learn more in Python’s documentation of classes.
- https://docs.python.org/3/tutorial/classes.html



raise

- Object-oriented program encourages you to encapusulate all the functionality of a class within the class definition. What if something goes wrong? What if someone tries to type in something random? What if someone tries to create a student without a name? Modify your code as follows:
- Notice how we check now that a name is provided and a proper house is designated. It turns out we can create our own exceptions that alerts the programmer to a potential error created by the user called raise. In the case above, we raise ValueError with a specific error message.
"""

class Student:
    def __init__(self, name, house):
        # We can use the __init__ and RAISE some errors in the init, to avoid fixing (try/except) the corner cases in the function call get_student()
        if not name: # if name == ""
            raise ValueError("Missing name")
            # print("Missing name")
            # sys.exit("Missing name") # too hard for exiting the code
            # return None # will jam the code because there are variables instantiated for the objects
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")

        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student(): # What'a abour bugs from user? name = "" (empty) or house == 'Puteiro'
    name = input("Name: ")
    house = input("House: ")
    # try:
    #     return Student(name, house)
    # except Value:
    #     ...
    return Student(name, house)

if __name__ == "__main__":
    main()

"""
- Notice how we check now that a name is provided and a proper house is designated. It turns out we can create our own exceptions that alerts the programmer to a potential error created by the user called raise. In the case above, we raise ValueError with a specific error message.
- It just so happens that Python allows you to create a specific function by which you can print the attributes of an object. Modify your code as follows:
"""

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
