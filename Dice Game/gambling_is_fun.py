import random


name = input("What is your name?")
dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)
print(f"How you doing {name}! You rolled a {dice_1} and a {dice_2}, and the total of youre rolls is {dice_1 + dice_2}.")
if dice_1 == dice_2:
    print("WOW you rolled a double! WOW WOW WOW WOWOWOWOWOWOW")
