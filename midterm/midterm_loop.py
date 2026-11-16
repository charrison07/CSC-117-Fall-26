# FILE NAME - midterm_loop.py

# NAME: CJ Harrison
# DATE: 11/2/26
# BRIEF DESCRIPTION:  

print("Welcome to the Mathenator2000")
print()

print("1. Compute area of a circle")
print("2. Compute area of a rectangle")
print()


choice = input("What is your choice?")
print()

if choice == "1":
    radius = float(input("What is the radius of a circle?"))

    area = 3.14 * radius  ** 2
    print (f"The area of the circle is {area}")
    print()
    again = input("Would you like to play again (y/n)?")
    while again == "y":
        radius = float(input("What is the radius of a circle?"))

        area = 3.14 * radius  ** 2
        print (f"The area of the circle is {area}")
        print()
        again = input("Would you like to play again (y/n)?")

    print("Thank you for using the Mathenator2000")



if choice == "2":
    length = float(input("What is the length of the rectangle? "))
    width = float(input("What is the width of the rectangle? "))
    area = (length * width)
    print(f"The area of the rectangle is {area}")
    print()
    print("Thank you for using the Mathenator2000")
