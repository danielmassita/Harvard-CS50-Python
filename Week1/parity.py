"""
x = int(input("What's x? "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
"""

def main():
    x = int(input("What's x? "))

    if is_even(x): # here we are calling the function...
        print("Even")
    else:
        print("Odd")



def is_even(n): # we take n as an argumment
#    return True if n % 2 == 0 else False # PYTHONIC 
    return (n % 2 == 0) # SUPER PYTHONIC 
""" 
    if n % 2 == 0:
        return True
    else:
        return False
"""
main()