# Demonstrates indexing into a list

students = [] # LIST
students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])

# Demonstrates iterating over a list

students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)


# Demonstrates iterating over and indexing into a list

students = ["Hermione", "Harry", "Ron"]

for stundent in range(len(students)):
    print(i + 1, students[i])

# len(students) return as an INT the number of indexes the variable/list students has. So in this case, len(students) return the INT 3 for we have 3 values os students. And the range() function accepts only INTegers, so we use the len() function to "grab" the number of elementes for index uses...


# Only with lists we could work too, but it can get messy when scaling up...

students = ["Hermoine", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Griffindor", "Slytherin"]

# Let's use DICT, as a kind of lists of lists...

students = {}

students = {

}

students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
print(students["Hermoine"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

"""
$ python hogwarts.py
Gryffindor
Gryffindor
Gryffindor
Slytherin
"""

# We can improve further our code, using KEY-VALUE

students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student)

"""
$ python hogwarts.py
Hermoine
Harry
Ron
Draco
"""

students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student])

"""
Hermoine Gryffindor
Harry Gryffindor
Ron Gryffindor
Draco Slytherin
"""

# Let's improve with sep=", "

students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student], sep=", ")

"""
Hermoine, Gryffindor
Harry, Gryffindor
Ron, Gryffindor
Draco, Slytherin
"""

# We can improve our idea of DICTs using default KEYs, so we can have every single different value analyzed...

students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

# And we can iterate through the same KEYs, and printing the VALUES

students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

"""
Hermoine, Gryffindor, Otter
Harry, Gryffindor, Stag
Ron, Gryffindor, Jack Russell terrier
Draco, Slytherin, None
"""

