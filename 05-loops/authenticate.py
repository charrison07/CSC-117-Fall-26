# FILE NAME - authenticate.py

# NAME: CJ Harrison
# DATE: 10/14/2026
# BRIEF DESCRIPTION: using a while loop to prompt the user for a password until it is guessed correctly
 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########
password = "tooManySecrets"
input_password = input("Enter password: ")

while input_password != password:
    print("Password does not match.")
    input_password = input("Enter password: ")

print("Access granted.")





########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Enter password: a

Password does not match.
Enter password: b

Password does not match.
Enter password: tooManySecrets

Access granted.
'''


'''
Enter password: tooManySecrets

Access granted.
'''


'''
Enter password: toomanysecrets

Password does not match.
Enter password: TOOMANYSECRETS

Password does not match.
Enter password: too_Many_Secrets

Password does not match.
Enter password: tooManySecrets

Access granted.
'''

