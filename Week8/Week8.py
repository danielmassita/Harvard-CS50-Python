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

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()
