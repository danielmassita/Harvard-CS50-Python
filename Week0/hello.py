# print("Hello, World!")
# print("Hello, name!")
input("What's your name? Who cares? No var here... ") # No data recorded @ any variable
# print("Hello, World")

# Ask user's name... #Recording the input from the user @ var name.
name = input("What's your name? ")

# Say hello to the user...
# print("Hello, name")
print("Hello, ") # By default, print() has an 'end=\n', so we can overwritte as end="" to avoid line break... Also we have sep=' ' for blank space as separtor.
print(name)

# Say hello to user in a better manner...
print("Hello, world!")
print('Hello, \"friend"') # Escape case \ before the "" to avoid closing the quotes.
print(" ")

name = input("What is your name again? ")
print("Hello," + name)
print("Hello, ",name)
print(f"Hello, {name}")

# If user uses too many spaces before and after name...
name = name.strip() # Strip blank spaces before and after strings...
print("Hello, without spaces, Mr./Ms. " + name)
name = name.capitalize() # Capitaliza only the first letter of the first word...
print("Hello, without spaces, and now capitalized Mr. " + name)
name = name.title() # Capitalize all the first letters of various words...
print("Hello, without spaces, and now capitalized, but in all the names Mr. " + name)
print(" ")

# I have used "Methods" in the variable name...
name = input("Finally, what is your full name (only two names)? ").strip().title()
print(f"Hello, Mr. {name}!")

# Split user's name into first name and last name, before=hand assignement...
firstName, lastName = name.split(" ")
print(f"Hello, {firstName}, or should I say Mr. {lastName}?")
