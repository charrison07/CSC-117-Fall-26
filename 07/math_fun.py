import random
#function to display welcome message
def display_message():
    print("Welcome to my add/subtract game!")
    print("Get ready for some math!")
#fucntion to ask the user if they would like to add or subtract
def add_or_subtract():
    response = input("Would you like to add or subtract?")
    if response == "add":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        print(f"What is {num1} + {num2}?")
    response_add = input("Enter your answer: ")
    if response_add == str(num1 + num2):
        print("Correct!")
    else:
        print("Incorrect. The answer is " + str(num1 + num2))
    if response == "subtract":
    
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        print(f"What is {num1} - {num2}?")
    response_subtract = input("Enter your answer: ")
    if response_subtract == str(num1 - num2):
        print("Correct!")
    else:
        print("Incorrect. The answer is " + str(num1 - num2))



def multiply_or_divide():
    response = input("Would you like to multiply or divide?")
    if response == "multiply":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        print(f"What is {num1} * {num2}?")
    response_multiply = input("Enter your answer: ")
    if response_multiply == str(num1 * num2):
        print("Correct!")
    else:
        print("Incorrect. The answer is " + str(num1 * num2))
    if response == "divide":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        print(f"What is {num1} / {num2}?")
    response_divide = input("Enter your answer: ")
    if response_divide == str(num1 / num2):
        print("Correct!")
    else:
        print("Incorrect. The answer is " + str(num1 / num2))
#add function
def add(a, b): 
    return a + b

#subtract function
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    else:
        return a / b
    
display_message()
add_or_subtract_or_multiply_or_divide = input("Would you like to add/subtract or multiply/divide? (Enter 'add/subtract' or 'multiply/divide'): ")