print("welcome to treasure Island")
print("your mission is to find treasure.\n")
choice1 = input('you\'re at a crossroad, where do you want to go? type "left" or "right"\n').lower()
if choice1 == "left":
    choice2 = input('you\'ve come to a lake there is an island in the middle of the lake. type "wait" to wait for a boat, type "swim"to swim across\n').lower()
    if choice2 == "wait":
        choice3 = input('you arrive at the island unharmed. there is a house with three doors. one "red" one "yellow" and one "blue".wich colour do you choose?').lower()
        if choice3 == "red":
            print("it's a room full of fire! game over.")
        elif choice3 == "yellow":
            print("you found the treasure! you win")
        elif choice3 == "blue":
            print("you enter a room of beasts! game over.")
        else:
            print("you choose a door that does not exist. game over!")
    else:
        print(" you got attacked by an angry trout. game over! ")
else:
    print("you fell into a hole. game over!")


