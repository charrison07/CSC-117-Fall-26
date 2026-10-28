# FILE NAME - calc.py

# NAME: 
# DATE: 
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience


########## ENTER YER CODE BELOW THIS LINE ##########
import calc_util

def main():
    print("Welcome to the Calculator")
    print()
    num1 = float(input("What is the first number? "))
    num2 = float(input("What is the second number? "))
    print()
    print(f"SUM =  {calc_util.add(num1, num2)}")
    print(f"DIFFERENCE =  {calc_util.subtract(num1, num2)}")
    print(f"PRODUCT =  {calc_util.multiply(num1, num2)}")
    print(f"QUOTIENT =  {calc_util.divide(num1, num2)}")
    print()
    print("Have a nice, mathy day.")
    print()
if __name__ == "__main__":
    main()
    









########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''

Welcome to the Calculator

What is the first number? 10
What is the second number? 5

SUM =  15.0
DIFFERENCE =  5.0
PRODUCT =  50.0
QUOTIENT =  2.0

Have a nice, mathy day.
'''


'''
Welcome to the Calculator

What is the first number? 0
What is the second number? 1

SUM =  1.0
DIFFERENCE =  -1.0
PRODUCT =  0.0
QUOTIENT =  0.0

Have a nice, mathy day.

'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 






2. How did you decide if the functions in the `calc_util` module should return or print?





'''
