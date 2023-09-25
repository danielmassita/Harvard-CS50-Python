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

class Student:
    def __init__(self, name, house):
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
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()

"""
- Notice how def __str__(self) provides a means by which a student is returned when called. Therefore, you can now, as the programmer, print an object, its attributes, or almost anything you desire related to that object.
- __str__ is a built-in method that comes with Python classes. It just so happens that we can create our own methods for a class as well! Modify your code as follows:
"""

class Student:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
            raise ValueError("Invalid patronus")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") or None
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()

"""
- Notice how we define our own method charm. Unlike dictionaries, classes can have built-in functions called methods. In this case, we define our charm method where specific cases have specific results. Further, notice that Python has the ability to utilize emojis directly in our code.
- Before moving forward, let us remove our patronus code. Modify your code as follows:
"""

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()

"""
- Notice how we have only two methods: __init__ and __str__.


Decorators

- Properties can be utilized to harden our code. In Python, we define properties using function “decorators”, which begin with @. Modify your code as follows:
- So here, too, in the spirit of programming a little more defensively, allow me to introduce
another feature of Python as well namely properties.
- So a property is really just an attribute that has even more defense mechanisms put into place, a little more functionality implemented
by you to prevent programmers, like me and you, from messing things up like these attributes. So again, a property is going to
be an attribute that you and I just have more control over. How? And how we're going to do that is going to use, in just a moment, a feature a keyword known as @property, which is technically a function. Property is a function in Python.
"""

class Student:

    def __init__(self, name, house):
        # if not name:
        #     raise ValueError("Invalid name")
        # if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
        #     raise ValueError("Invalid house")
        self.name = name
        self.house = house # NOT USE _ here so we use only ONE Error Check at @house.setter

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter - Aqui eu PEGO!
    @property
    def house(self):
        return self._house

    # Setter - Aqui eu DEFINO! Again, Error Checking when we call the function
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")

        self._house = house

    # When we call main(), and try to circumvent the default (using student.house = "blablabla"), we CREATE a step-by-step functions calls to order things up!
    # Python reads the script, goes through __init__, __str__, Getter, Setter, main().

def main():
    student = get_student()
#    student.house = "Number Four, Privet Drive" # When we try to assign new value student.house... We CALL BACK @property and @setter.house
    print(student)

    # But because Python knows that, wait a minute, you're trying to assign that is, set a value and that value, a.k.a. house, is now defined as a property you're going to have to go through the setter function instead to even let you change that value. And because I have this raise ValueError. If the house is not as intended, you're not going to be allowed to change it to an invalid value. So I'm protecting the data on the way in, through the init method, and I'm even defending the data if you try to override it there. So I think the only solution for me, the programmer, is, don't try to break my own code. Let me remove that line because it's just not going to work.

    # I don't want you to be able to go in there and just change them at will. I want to have some control over that object so that you can just trust that it's going to be correct as designed. So using a getter and setter really just enables Python to automatically detect when you're trying to manually set a value. The equal sign and the dot, as I've highlighted here, is enough of a clue to Python to realize, wait a minute, Let me see if this class has a setter defined. And if so, I'm going to call that, and I'm not just going to blindly assign the value from right to left. So it's just giving me more control.

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        # if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
        #     raise ValueError("Invalid house")
        # With getter @property and setter @house.setter we don't need anymore the error check in __init__
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


    # GETTER is a function for a class that gets some attributes (we use @property)
    @property
    def house(self):
        return self._house

    # SETTER is a function in some class that sets some value (we use @house.setter)
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
#    student.house = "Number Four, Privet Drive" # We can access this instance variable using DOT NOTATION
    print(student) # The line above circumvent the IF conition and the other Error Checking (__init__) so we can escape the first __init__ from Class initialization, but when main() is called, we change the variable (with student.house = 'new data')...
    # Classes create control, but not prevent user/developer of messing up the code (we need to work more defensively)
    # Let's use PROPERTIES! to prevent programmers of messing up these attributes
    # Decorators are functions that modify the behaviour of other functions

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()

"""
- Notice how we’ve written @property above a function called house. Doing so defines house as a property of our class. With house as a property, we gain the ability to define how some attribute of our class, _house, should be set and retrieved. Indeed, we can now define a function called a “setter”, via @house.setter, which will be called whenever the house property is set—for example, with student.house = "Gryffindor". Here, we’ve made our setter validate values of house for us. Notice how we raise a ValueError if the value of house is not any of the Harry Potter houses, otherwise, we’ll use house to update the value of _house. Why _house and not house? house is a property of our class, with functions via which a user attempts to set our class attribute. _house is that class attribute itself. The leading underscore, _, indicates to users they need not (and indeed, shouldn’t!) modify this value directly. _house should only be set through the house setter. Notice how the house property simply returns that value of _house, our class attribute that has presumably been validated using our house setter. When a user calls student.house, they’re getting the value of _house through our house “getter”.
- In addition to the name of the house, we can protect the name of our student as well. Modify your code as follows:
"""

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()


"""
- Notice how, much like the previous code, we provide a getter and setter for the name.

- You can learn more in Python’s documentation of methods.
- https://docs.python.org/3/tutorial/classes.html



"""
