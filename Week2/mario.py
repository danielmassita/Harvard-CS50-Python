# Prints a column of bricks

print("#")
print("#")
print("#")

# Prints column of bricks using a loop

for _ in range(3):
    print("#")


# Prints column of bricks using a function with a loop

def main():
    print_column(3)


def print_column(height):
    for _ in range(height):
        print("#")

main()

# Prints column of bricks using a function with str multiplication

def main():
    print_column(3)


def print_column(height):
    print("#\n" * height, end="")

main()

# Print row of coins using a function with str multiplication

def main():
    print_row(4)


def print_row(width):
    print("?" * width)

main()


# Prints square of bricks using a function with nested loops

def main():
    print_square(3)


def print_square(size):
    
    for i in range(size): # For each row in square (n-sized)
        for j in range(size): # We iterate for each brick in the row (like, size x size)
            print("#", end="") # We iterate and print a brick, like # # # three times in another row...
        print() # Print blank line


main()


# Prints square of bricks using a function with str multiplication

def main():
    print_square(3)

def print_square(size):
    for _ in range(size):
        print("#" * size)

main()


# Notice that we have an outer loop addresses each row in the square. Then, we have an inner loop that prints a brick in each row. Finally, we have a print statement that prints a blank line.
# We can further abstract away our code:

def main():
    print_square(3)

def print_square(size):
    for _ in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()

"""
###
###
###
"""

def main():
    print_square(6)

def print_square(size):
    for _ in range(size):
        print_row(size)

def print_row(width):
    print("?" * width)

main()

"""
??????
??????
??????
??????
??????
??????
"""

