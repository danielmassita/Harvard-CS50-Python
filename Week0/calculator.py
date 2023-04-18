x = input("What is the value for X? ") # Inputs are always strings by default...
y = input("What is the value for Y? ")
z = x + y
print(z) # The error is because we are concatenating values as strings, by default...

z = int(x) + int(y)
print(z)
print(int(x) + int(y)) # It also works with less lines of code...

# It turns out that INT is used for interger numbers and FLOAT are used for decimal real numbers...
a = float(input("What is the value for A? Eg.: 999 "))
b = float(input("What is the value for B? Eg.: 1 "))
c = round(a + b) # as in 1,000 one thousand US Style
print(f"{c:,}") # I'm using the format f and applying the , as a thousand separator so I use :, after the variable...

# round(number[, ndigits]) [optional, digits after comma to round] :: round(number[, 2]) rounds up to 2 decimal places

g = float(input("What is the value for G? "))
h = float(input("What is the value for H? "))
i = round(g / h, 2) # Will round the FLOAT in two decimal places...

print(i)
print(f"{i:.3f}") # Will round the FLOAT in three decimal places but in a more cryptic way as .3f
# We used F-String to say how many digits I want...
