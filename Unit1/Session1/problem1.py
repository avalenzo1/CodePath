def welcome():
    print("Welcome to The Hundred Acre Wood!")
    
def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

def print_catchphrase(character):
	if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

welcome()
greeting("Michael")
greeting("Winnie the Pooh")

character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)