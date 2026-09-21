# FILE NAME - dice.py

# NAME: CJ Harrison
# DATE: 9/21/26
# BRIEF DESCRIPTION: Rolling two dice with a seed



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random


########## ENTER YER CODE BELOW THIS LINE ##########


random_seed = int(input("Enter a seed for the random number generation: "))
random.seed(random_seed)
dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)
print(f"Die roll one is {dice_1}")
print(f"Die roll two is {dice_2}")


########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
Die roll one is 5
Die roll two is 2

'''



'''

Enter a seed for the random number generation: 22
Die roll one is 2
Die roll two is 2

'''



'''

Enter a seed for the random number generation: -30
Die roll one is 5
Die roll two is 3

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is the purpose of "seeding" the random number generator?
the purpose of seeding the random number generator is to ensure that the sequence of random numbers generated can be reproduced. 



'''
