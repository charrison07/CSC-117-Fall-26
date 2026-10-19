# FILE NAME - password_strength_test.py

# NAME: CJ Harrison
# DATE: 10/14/2026
# BRIEF DESCRIPTION: making a password strength checker that rates the strength of a password based on length, character variety, and provides suggestions for improvement. 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########
print("===== PASSWORD STRENGTH CHECKER =====")
print("This tool analyzes your password and rates its strength.\n")
password = input("Enter a password to check: ")
points = 0
length = len(password)
if length >= 12:
    points += 25
elif length >= 8:
    points += 15
elif length >= 6:
    points += 10

uppercase_count = 0
lowercase_count = 0
digit_count = 0
special_count = 0

for letter in password:
    if letter.isupper():
        uppercase_count += 1
    elif letter.islower():
        lowercase_count += 1
    elif letter.isdigit():
        digit_count += 1
    elif letter in "!@#$%^&*()-_=+[]{}|;:'\\\",.<>/?":
        special_count += 1
character_points = 0
if uppercase_count >= 1:
    points += 15
    character_points += 1
if lowercase_count >= 1:
    points += 15
    character_points += 1
if digit_count >= 1:
    points += 15
    character_points += 1
if special_count >= 1:
    points += 15
    character_points += 1

if character_points >= 3:
    points += 15

if points >= 80:
    strength = "STRONG"
elif points >= 60:
    strength = "MODERATE"
elif points >= 40:
    strength = "WEAK"
else:
    strength = "VERY WEAK"





print("===== PASSWORD ANALYSIS =====")
print(f"Length: {length} characters")
print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"Digits: {digit_count}")
print(f"Special characters: {special_count}")
print(f"\nSecurity Score: {points}/100")
print(f"Strength Assessment: {strength}\n")

print("===== IMPROVEMENT SUGGESTIONS =====")
if points >= 80:
        print("- Excellent password! Remember to use different passwords for different accounts.")

if points < 100:
    if length < 12:
        print("- Use at least 12 characters for better security")
    if uppercase_count == 0:
        print("- Add uppercase letters (A-Z)")
    if lowercase_count == 0:
        print("- Add lowercase letters (a-z)")
    if digit_count == 0:
        print("- Add numbers (0-9)")
    if special_count == 0:
        print("- Add special characters (!@#$%^&*)")
   
    



      








########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
===== PASSWORD STRENGTH CHECKER =====
This tool analyzes your password and rates its strength.

Enter a password to check: password

===== PASSWORD ANALYSIS =====
Length: 8 characters
Uppercase letters: 0
Lowercase letters: 8
Digits: 0
Special characters: 0

Security Score: 30/100
Strength Assessment: VERY WEAK

===== IMPROVEMENT SUGGESTIONS =====
- Use at least 12 characters for better security
- Add uppercase letters (A-Z)
- Add numbers (0-9)
- Add special characters (!@#$%^&*)
'''


'''
This tool analyzes your password and rates its strength.

Enter a password to check: p@SSword!

===== PASSWORD ANALYSIS =====
Length: 9 characters
Uppercase letters: 2
Lowercase letters: 5
Digits: 0
Special characters: 2

Security Score: 75/100
Strength Assessment: MODERATE

===== IMPROVEMENT SUGGESTIONS =====
- Use at least 12 characters for better security
- Add numbers (0-9)
'''


'''
===== PASSWORD STRENGTH CHECKER =====
This tool analyzes your password and rates its strength.

Enter a password to check: 4$DL_dsa_dsf!#

===== PASSWORD ANALYSIS =====
Length: 14 characters
Uppercase letters: 2
Lowercase letters: 6
Digits: 1
Special characters: 5

Security Score: 100/100
Strength Assessment: STRONG

===== IMPROVEMENT SUGGESTIONS =====
- Excellent password! Remember to use different passwords for different accounts.
'''
