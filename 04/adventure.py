import random


#game starts as an adventure, where the player will be asked their name and class. (can be anything, doesnt affect the gameplay)
print ("Welcome to the python adventure game!")
name = input("What is your name? ")
char_class = input("What is your class? ")

print(f"Welcome, {name} the {char_class}!")

#introduce the adventure scenario

print("You come to a fork in the road, which direction will you go?")
choice = input("Do you want to go left or right? (left/right) ")
if choice.lower() == "left":
    print("You encounter a mysterious cave!")
    print("You find yourself in a dark forest. The trees are tall and the path is unclear.")
print("                                 XXX                          ")
print("                                XX XX                         ")
print("                                X   X                         ")
print("                            XXX    XXX                      ")
print("                           XX        XX                     ")
print("                         XXX          XXX                  ")
print("                         X              X                  ")
print("                     XXXXXXXXXXXXXXXXXXXXXXX               ")
print("                    XX                      XX             ")
print("                   XX                        XX            ")
print("                  XX                          X           ")
print("               XXXX      XXXXXXXXXXXXXXXXX    XXXX        ")
print("             XX        XX                XX      XXX       ")
print("           xx         xx                   x       xx      ")
print("        XXX          XX                    XX       XX      ")
print("       XX         XXXX                      XX       XX     ")
print("      XX          X                          XX       XXX   ")
print("    XXX          X                            XX        XX  ")
print("   XX           XX                              XX       X  ")
print("  XX          XXX                                XX      XX ")
print(" XX          XX                                   XX     XX")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("inside of the cave there is a huge dragon! its too strong to take on your own!")
print("You must find a way to defeat it or escape!")
print("What will you do?")
action = input("Do you want to fight or flee? (fight/flee) ")
if action.lower() == "fight":
    print("You are defeated and the adventure ends.")
    print("THE END")
    print("You are defeated and the adventure ends.")
    quit()
elif action.lower() == "flee":
    print("You run out of the cave, escaping the dragon!")
    print("You survive, you have saved the kingdom and can now rest.")
    print("THE END")
    quit()
elif choice.lower() == "right":
    print("You encounter a large castle!")
    print("         -|                  [-_-_-_-_-_-_-_-]                  |-")
    print("         [-_-_-_-_-]          |             |          [-_-_-_-_-]")
    print("          | o   o |           [  0   0   0  ]           | o   o |")
    print("           |     |    -|       |           |       |-    |     |")
    print("           |     |_-___-___-___-|         |-___-___-___-_|     |")
    print("           |  o  ]              [    0    ]              [  o  |")
    print("           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________")
    print("_____----- |     ]              [ ||||||| ]              [     |")
    print("           |     ]              [ ||||||| ]              [     |")
    print("       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_")
    print("       __________------------_____________-------------_________")

#https://www.asciiart.eu/art/c1d67a87c6ec2232

print("You enter and see a lone pillar with a button, it says 1/2. What will you do?")
choice = int(input("Do you want to press the button or leave it alone? (1/2) "))
if choice == 1:
    random.randint(1, 2)
    if random.randint(1, 2) == 1:
        print("You press the button and a secret passage opens!")
        print("You enter the passage and find a treasure!")
        print("THE END")
        quit()
    else:
        print("Uh oh! The button does nothing!")
        print("you are disapointed but survive")
        print("THE END")
        quit()
elif choice == 2:
    print("You leave the button alone and continue exploring the castle.")
    print("THE END")
    quit()
else:
    print("You are lost and wander aimlessly in the forest, you stumble on a branch and die!")
    print("THE END")
    quit()
