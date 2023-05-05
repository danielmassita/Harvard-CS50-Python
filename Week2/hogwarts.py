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


