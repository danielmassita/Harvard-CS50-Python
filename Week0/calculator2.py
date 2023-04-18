def main(): 
  x = int(input("What is X? "))
  print("X squared is", square(x))
  
  
def square(n):
  return n * n
  # return n ** 2 (squared two)
  # return pow(n, 2) raise n to it's 2 power
  
main()
