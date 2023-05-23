import sys

"""
print("Hello, my name is", sys.argv[1]) # [0] is py name.py 
print(sys.argv[0]) # name.py
print(sys.argv[1]) # Daniel
print(sys.argv[0:2])
"""

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")



if len(sys.argv) < 2: 
    print("Too few arguments")
elif len(sys.argv) >2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1]) # py name.py "Daniel Massita" == str[1]

