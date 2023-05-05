# Demonstrates multiple (identical) function calls
print("meow")
print("meow")
print("meow")

# Demonstrates a while loop, counting down
i = 3
while i != 0:
    print("meow")
    i = i - 1

# Demonstrates a while loop, counting up from 1
i = 1
while i <= 3:
    print("meow")
    i = i + 1

# Demonstrates a while loop, counting up from 0
i = 0
while i < 3:
    print("meow")
    i = i + 1

# Demonstrates (more succinct) incrementation 
i = 0
while i < 3:
    print("meow")
    i += 1

# Demonstrates a for loop, using a list
for i in [0, 1, 2]:
    print("meow")

# Demonstrates a for loop, using range
for i in range(3):
    print("meow")

# Demonstrates a for loop, with _ as a variable
for _ in range(3):
    print("meow")

# Demonstrates str multiplication
print("meow\n" * 3, end="") # To avoid 'meowmeowmeow' we break line after each 'meow', but in the end we end without breaking line end=""





# Introduces continue, break

while True:
    n = int(input("What's n? "))
    if n <= 0: # if the input from user is less or zero, we keep the user in a infinity trap asking for the input
        continue
    else: # when the users coop, we break the infinity loop trap
        break
for _ in range(n): 
    print("meow")



