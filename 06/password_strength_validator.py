# FILE NAME - password_strength_analyzer.py

# NAME: CJ Harrison
# DATE: 10/22/26
# BRIEF DESCRIPTION: using way too many if statements



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience


import random


########## ENTER YER CODE BELOW THIS LINE ##########

password = input("Enter your password: ")


counts = [0, 0, 0, 0]

for character in password:
    if character.isupper():
        counts[0] += 1
    elif character.islower():
        counts[1] += 1
    elif character.isdigit():
        counts[2] += 1
    else:
        counts[3] += 1

length = len(password)


if length < 8:
    length_points = 0
elif length <= 15:
    length_points = 5
else:
    length_points = 8


points = [length_points]

for count in counts:
    if count == 0:
        points.append(0)
    elif count == 1:
        points.append(2)
    elif count == 2:
        points.append(4)
    else:
        points.append(8)


total_points = sum(points)
score = total_points / 40
percentage = score * 100


print()
print("Password Analysis Report")
print("-------------------------")
print(f"LENGTH: {points[0]} points ({length} characters)")
print(f"UPPERCASE: {points[1]} points ({counts[0]} uppercase letter(s))")
print(f"LOWERCASE: {points[2]} points ({counts[1]} lowercase letter(s))")
print(f"NUMBERS: {points[3]} points ({counts[2]} number(s))")
print(f"SPECIAL CHARACTERS: {points[4]} points ({counts[3]} special character(s))")
print()
print(f"Total Score: {score}")
print(f"Strength Percentage: {percentage}%")





########### END YER CODE ABOVE THIS LINE ###########










########################################
#          SAMPLE OUTPUT
########################################

'''
Enter your password: password

Password Analysis Report
-------------------------
LENGTH: 5 points (8 characters)
UPPERCASE: 0 points (0 uppercase letter(s))
LOWERCASE: 8 points (8 lowercase letter(s))
NUMBERS: 0 points (0 number(s))
SPECIAL CHARACTERS: 0 points (0 special character(s))

Total Score: 0.325
Strength Percentage: 32.5%
'''

'''
Enter your password: p@$$WORD

Password Analysis Report
-------------------------
LENGTH: 5 points (8 characters)
UPPERCASE: 8 points (4 uppercase letter(s))
LOWERCASE: 2 points (1 lowercase letter(s))
NUMBERS: 0 points (0 number(s))
SPECIAL CHARACTERS: 8 points (3 special character(s))

Total Score: 0.575
Strength Percentage: 57.49999999999999%
'''

'''
Enter your password: 123PASwor

Password Analysis Report
-------------------------
LENGTH: 5 points (9 characters)
UPPERCASE: 8 points (3 uppercase letter(s))
LOWERCASE: 8 points (3 lowercase letter(s))
NUMBERS: 8 points (3 number(s))
SPECIAL CHARACTERS: 0 points (0 special character(s))

Total Score: 0.725
Strength Percentage: 72.5%
'''

'''
Enter your password: 123pasWOR!@#

Password Analysis Report
-------------------------
LENGTH: 5 points (12 characters)
UPPERCASE: 8 points (3 uppercase letter(s))
LOWERCASE: 8 points (3 lowercase letter(s))
NUMBERS: 8 points (3 number(s))
SPECIAL CHARACTERS: 8 points (3 special character(s))

Total Score: 0.925
Strength Percentage: 92.5%
'''

'''
Enter your password: 123pasWOR!@#888888888888

Password Analysis Report
-------------------------
LENGTH: 8 points (24 characters)
UPPERCASE: 8 points (3 uppercase letter(s))
LOWERCASE: 8 points (3 lowercase letter(s))
NUMBERS: 8 points (15 number(s))
SPECIAL CHARACTERS: 8 points (3 special character(s))

Total Score: 1.0
Strength Percentage: 100.0%
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. This is one of your first experiences with larger programs - what are three things
   that were challenging for you?







'''



########################################
#            ATTESTATION
########################################

'''
It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[ ] I'm solid. Totally got it.

'''