
import random


# My Github IDE kept adding the distro line automatically, which is why codegrade kept failing

# You need to add at least five more insults (for a total of at least six)
# Insert your insults into the strings in the list.
insults = [
    'You look like a bunch of rocks',
    'A',
    'B',
    'C',
    'D',
    'E'
]

def welcome():
    '''
    This function should output four lines (three lines of text as described in the SAMPLE OUTPUT and one blank line).
    '''    
    print("---------------------------------")
    print("Welcome to the Insulternator 3500")
    print("---------------------------------")
    print()



def show_all_insults():
    '''
    This function simply outputs the values in the list called 'insults'.
    '''
    print(insults)


def one_insult():
    '''
    This function will print one insult from the list at random using `random.choice()`.
    '''
    print(random.choice(insults))

    
def two_insults():
    '''
    This function will print two insults from the list at random. NEEDS to call `one_insult()` twice.
    '''
    one_insult()
    one_insult()


def insult_specific_name(name):
    '''
    This function takes in a name from the main program and then will personlize an insult chosen at random from the list.
    '''
    print(f"{name}, here is your insult: {random.choice(insults)}")

def insult_x_number_of_insults(num):
    '''
    This function takes in one variable, `num`, and will dispense that number of insults at random from the list.
    '''
    for i in range(num):
        one_insult()

def goodbye():
    '''
    This function should output four lines (one blank line and three lines of text as described in the SAMPLE OUTPUT).
    '''    
    print()
    print("---------------------------------------------")
    print("Thank you for playing the Insulternator 3500!")
    print("---------------------------------------------")
    




