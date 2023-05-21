x = int(input("What's x? "))
print(f"The value of x is {x}.")



# VALUE ERROR

"""
>>> x = int(input("What's x? "))
What's x? 10

>>> x = int(input("What's x? "))
What's x? cat

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'cat'
"""



# TRY

try: 
    x = int(input("What's x? "))
    print(f"The value of x is {x}.")
except ValueError:
    print("We have a ValueError, for x is not an INTeger.")

