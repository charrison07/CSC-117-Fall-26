# FILE NAME - while_loop_guess_high_low.py

# NAME: CJ Harrison
# DATE: 10/14/2026
# BRIEF DESCRIPTION:  using a while loop to display the amount of tries it took to guess a secret number and give hints if the guess was too high or too low.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience







########## ENTER YER CODE BELOW THIS LINE ##########
SECRET_NUMBER = 33
guess = 0
tries = 0

while guess != SECRET_NUMBER:
    guess = int(input("Guess a number: "))
    tries += 1
    if guess < SECRET_NUMBER:
        print("Your guess is too low.")
    elif guess > SECRET_NUMBER:
        print("Your guess is too high.")

print("You guessed in", tries, "tries.")





########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Guess a number: 22
Your guess is too low.

Guess a number: 44
Your guess is too high.

Guess a number: 33

You guessed in 3 tries.
'''


'''
Guess a number: 33

You guessed in 1 tries.
'''


'''
Guess a number: -9
Your guess is too low.

Guess a number: 100
Your guess is too high.

Guess a number: 30
Your guess is too low.

Guess a number: 32
Your guess is too low.

Guess a number: 34
Your guess is too high.

Guess a number: 33

You guessed in 6 tries.
'''

