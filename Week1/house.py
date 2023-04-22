name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slythering")
else: 
    print("Who!?")



if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slythering")
else: 
    print("Who!?")



match name: # samesame Switch-Case-Break from JavaScript
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # _ same as default from Switch-Case from JS...
        print("Who!?")



match name: # samesame Switch-Case-Break from JavaScript
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # _ same as default from Switch-Case from JS...
        print("Who!?")
