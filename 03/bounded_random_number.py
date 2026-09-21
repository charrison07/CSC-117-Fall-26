# FILE NAME - bounded_random_number.py

# NAME: CJ Harrison
# DATE: 9/21/26
# BRIEF DESCRIPTION: using a random generated bound number to generate a random number 1-10 based on a seed the user enters



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random


########## ENTER YER CODE BELOW THIS LINE ##########


random_seed = int(input("Enter a seed for the random number generation: "))
random.seed(random_seed)
print(random.randint(1, 10))

########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
10

'''



'''

Enter a seed for the random number generation: 32
2

'''



'''

Enter a seed for the random number generation: 100
3

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is a good way to remember if the arguments (parameters) for a bounded number are inclusive or exclusive?
one way is looking at if they have brackets (inclusive) or parenthesis (exclusive). 





'''
