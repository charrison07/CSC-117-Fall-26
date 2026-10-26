# FILE NAME - mfa_simulator.py

# NAME: CJ Harrison
# DATE: 10/22/26
# BRIEF DESCRIPTION: using a random seed to simulate a multi-factor authentication system, while using a list and a for loop.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience


import random


########## ENTER YER CODE BELOW THIS LINE ##########
seed = int(input("ENTER SEED FOR SIMULATION: "))
random.seed(seed)
print()
print("===============================")
print("  SIMULATING CODE GENERATION   ")
print("===============================")
backup_codes = []

for i in range(10):
    code = random.randint(100000, 999999)
    backup_codes.append(code)
    print("Backup code:", code)

print()
print("===============================")
print("     SIMULATING CODE USE       ")
print("===============================")
print()

print("You have 10 codes remaining.")
code = int(input("Enter a valid code: "))
if code in backup_codes:
    print()
    print("Access Granted")
    backup_codes.remove(code)
    print()
    print("You have", len(backup_codes), "codes remaining.")
else:
    print()
    print("Access Denied")

for code in backup_codes:
    print("Backup code:", code)











########### END YER CODE ABOVE THIS LINE ###########










########################################
#          SAMPLE OUTPUT
########################################

'''
ENTER SEED FOR SIMULATION: 33

===============================
  SIMULATING CODE GENERATION   
===============================

Backup code: 698032
Backup code: 275378
Backup code: 762944
Backup code: 344546
Backup code: 956690
Backup code: 981604
Backup code: 390760
Backup code: 602233
Backup code: 783524
Backup code: 658550

===============================
     SIMULATING CODE USE       
===============================

You have 10 codes remaining.
Enter a valid code: 123456

Access Denied
'''


'''
ENTER SEED FOR SIMULATION: 33

===============================
  SIMULATING CODE GENERATION   
===============================

Backup code: 698032
Backup code: 275378
Backup code: 762944
Backup code: 344546
Backup code: 956690
Backup code: 981604
Backup code: 390760
Backup code: 602233
Backup code: 783524
Backup code: 658550

===============================
     SIMULATING CODE USE       
===============================

You have 10 codes remaining.
Enter a valid code: 344546

Access Granted

You have 9 codes remaining.

Backup code: 698032
Backup code: 275378
Backup code: 762944
Backup code: 956690
Backup code: 981604
Backup code: 390760
Backup code: 602233
Backup code: 783524
Backup code: 658550
'''


'''
ENTER SEED FOR SIMULATION: 0

===============================
  SIMULATING CODE GENERATION   
===============================

Backup code: 985440
Backup code: 503958
Backup code: 894772
Backup code: 541001
Backup code: 142450
Backup code: 371493
Backup code: 636110
Backup code: 609532
Backup code: 524604
Backup code: 921872

===============================
     SIMULATING CODE USE       
===============================

You have 10 codes remaining.
Enter a valid code: 985440

Access Granted

You have 9 codes remaining.

Backup code: 503958
Backup code: 894772
Backup code: 541001
Backup code: 142450
Backup code: 371493
Backup code: 636110
Backup code: 609532
Backup code: 524604
Backup code: 921872
'''




########################################
#          REFLECTION QUESTIONS
########################################

'''

1. This program had multiple steps - what was the hardest for you?
the for loop







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