## Gives the ASCII code for a character, or a character from an ASCII code

# Get the ASCII code for a given character
def getASCII(x):
    ascii = ord(x)
    print(f"The ASCII value for character {x} is: {str(ascii)}")

# Get the character for a given ASCII code
def getLetter(x):
    character = chr(x)
    print(f"{x} is the ASCII value for character: {str(character)}")

option = True
while option: # infinate loop until code or character is entered
    choice = input("Do you want to check a character or code? ").lower()
    if choice != "character" and choice != "code": # checking input
        print("Invalid response.")
        continue
    elif choice == "character":
        option = False
        check = input("What character do you want to check? ") # obtaining and checking character
        getASCII(check)
    elif choice == "code":
        option = False
        check = int(input("What code would you like to check? ")) # obtaining and checking ascii code
        getLetter(check)
    else:
        print("There has been an error. The program will now stop running.") # error
        option = False
        break
