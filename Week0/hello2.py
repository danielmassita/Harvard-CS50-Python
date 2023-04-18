def main():
  name = input("What's your name? ")
  hello(name) # nothing happens if no called... 

  

def hello(to="world"): #to="world" will use world as default value if none specified...  
  print("Hello,", to)
  

main() # so in the end, we call all the main() functions up above...
