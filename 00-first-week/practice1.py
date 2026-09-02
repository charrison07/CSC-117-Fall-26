print ("hi there!")
name = input("what is your name?")
print (f"whats up {name}!")
food = input("what is your favorite food?")
print (f"ah thats awesome! i love {food} too!")
# move onto next question
choice = input("do you prefer pizza or wings?")
if choice == "wings":
    sauces = input("what sauces do you want with your wings?")
    print(f"okay, {sauces} will be your sauces!")