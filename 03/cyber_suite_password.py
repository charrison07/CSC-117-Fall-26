# FILE NAME - cyber_suite_password.py

# NAME: CJ Harrison 
# DATE: 9/23/26
# BRIEF DESCRIPTION: using strings and random to creatae a random password using a seed



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random
import string


########## ENTER YER CODE BELOW THIS LINE ##########


random_seed = int(input("Enter a seed for the random number generation: "))
random.seed(random_seed)



X1 = random.choice("!@#$&(),-_")
X2 = random.choice(string.ascii_lowercase)
X3 = random.choice(string.ascii_uppercase)
X4 = random.choice(string.ascii_lowercase)
X5 = random.choice(string.ascii_uppercase)
X6 = random.choice(string.digits)
X7 = random.choice(string.digits)
X8 = random.choice("!@#$&(),-_")
print(f"Your random password is: {X1}{X2}{X3}{X4}{X5}{X6}{X7}{X8}")


########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
Your random password is:
_fUhI78-

'''



'''

Enter a seed for the random number generation: 22
Your random password is:
#hAtO21(

'''



'''

Enter a seed for the random number generation: 0
Your random password is:
)yNbI87)

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab?
figuring out how to output the values together





2. What value do you see in the `string` module?
I like how it teaches how to use characters and variables in strings





'''
