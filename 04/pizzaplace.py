pizza = int(input("Welcome to Pizza D's! What size pizza would you like? (1-3):"))
if pizza == 1:
    print("You ordered a small pizza.")
elif pizza == 2:
    print("You ordered a medium pizza.")
elif pizza == 3:
    print("You ordered a large pizza.")
else:
    print("Invalid choice.")
    quit()
topping = input("Would you like to add toppings? (y/n): ")
if topping == "y" or topping == "yes":
    topping2 = input("What toppings would you like? (cheese/pepperoni): ")
    if topping2 == "cheese":
        print("You have added cheese.")
    elif topping2 == "pepperoni":
        print("You have added pepperoni.")
    else:
        print("Invalid topping choice.")
        quit()
else:
    print("No toppings added.")

if pizza == 1 and topping == "y":
    print("You have ordered a small pizza with toppings, That will be $9.99")
elif pizza == 2 and topping == "y": 
    print("You have ordered a medium pizza with toppings, That will be $12.99")
elif pizza == 3 and topping == "y": 
    print("You have ordered a large pizza with toppings, That will be $15.99")

if pizza == 1 and topping == "n":
    print("You have ordered a small pizza without toppings, That will be $8.99")
elif pizza == 2 and topping == "n":
    print("You have ordered a medium pizza without toppings, That will be $11.99")
elif pizza == 3 and topping == "n":
    print("You have ordered a large pizza without toppings, That will be $14.99")

