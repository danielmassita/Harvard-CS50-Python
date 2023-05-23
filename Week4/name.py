import sys

"""
print("Hello, my name is", sys.argv[1]) # [0] is py name.py 
print(sys.argv[0]) # name.py
print(sys.argv[1]) # Daniel
print(sys.argv[0:2])
"""

#try:
#    print("Hello, my name is", sys.argv[1])
#except IndexError:
#    print("Too few arguments")


"""
if len(sys.argv) < 2: 
    print("Too few arguments")
elif len(sys.argv) >2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1]) # py name.py "Daniel Massita" == str[1]
"""

# Check for errors
if len(sys.argv) < 2: 
    sys.exit("Too few arguments")
"""elif len(sys.argv) >2:
    sys.exit("Too many arguments")"""

# Print name tags, assuming check sys.argv already done (otherwise, it should sys.exit)
print("Hello, my name is >>> (pre-game)", sys.argv[1]) # py name.py "Daniel Massita" == str[1]

for name in sys.argv[1:]: # [1:] starts at index 1, not 0, until the end with the slice method
    print("Hello, my name is", name)