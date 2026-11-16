# FILE NAME - midterm_results.py

# NAME: CJ Harrison
# DATE: 11/2/26
# BRIEF DESCRIPTION:  


results = []

# WRITE YOUR CODE HERE
# MEET REQUIREMENTS AS STATED IN BRIGHTSPACE


print("Welcome to the Mathenator2000")
print()
print("Please choose from the following menu:")

print("1. Compute area of a circle")
print("2. Compute area of a rectangle")
print()


choice = input("What is your choice?")
print()

if choice == "1":
    radius = float(input("What is the radius of a circle?"))

    area = 3.14 * radius  ** 2
    results.append(area)
    print (f"The area of the circle is {area}")
    print()
    again = input("Would you like to play again (y/n)?")
    while again == "y":
        radius = float(input("What is the radius of a circle?"))

        area = 3.14 * radius  ** 2
        results.append(area)
        print (f"The area of the circle is {area}")
        print()
        again = input("Would you like to play again (y/n)?")

    while again == "n":
         print()
print("-------------------------")
print("A record of your results:")
for result in results:
      print(result, end=" ")
print()
print("Thank you for using the Mathenator2000")




if choice == "2":
    length = float(input("What is the length of the rectangle? "))
    width = float(input("What is the width of the rectangle? "))
    area = (length * width)
    results.append(area)
    print(f"The area of the rectangle is {area}")
    print()
    again = input("Would you like to play again (y/n)?")
    while again == "y":
        length = float(input("What is the length of the rectangle? "))
        width = float(input("What is the width of the rectangle? "))
        area = (length * width)
        results.append(area)
        print(f"The area of the rectangle is {area}")
        print()
        again = input("Would you like to play again (y/n)?")
    while again == "n":
        print()
        print("-------------------------")
        print("A record of your results:")
        for result in results:
            print(result, end=" ")
            print()

        print("Thank you for using the Mathenator2000")
        break

if choice == "3":
    print("Invalid selection")
    again = input("Would you like to play again (y/n)?")

    while again == "n":

        print()
        print("-------------------------")
        print("A record of your results:")
        for result in results:
               print(result, end="[]")
               print()
               
        print("Thank you for using the Mathenator2000")
        break

       




    