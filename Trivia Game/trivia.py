def welcome():
    print("Welcome to the NYG Trivia Game!")
    name = input("What is your name? ")
    print(f"Hello, {name}!  Each question is worth 10 points, with retrys being 5.  Good luck!")
    return name

n = welcome()

def quiz():


    questions = ["What is the name of the Giants Starting QB?", "What is the name of the Giants Wide Receiver?", "What is the name of the Giants Running Back?", "What is the name of the Giants Tight End?", "What is the name of the Giants Head Coach?"]
    answers= ["JJ McCarthy", "Malik Nabers", "Cam Skattebo", "Isaiah Likely", "John Harbaugh"]

    score = 0
    i = 0
    for question in questions:
        response = input(f"{question} ")
        if response == answers[i]:
            print("Correct!")
            score += 10
            print(f"Awesome! 10 points! Your score is now {score}.")
        else:
            print("Incorrect!  You have one more chance to answer the question.")
            response = input(f"{question} ")
            if response == answers[i]:
                print("Correct!")
                score += 5
                print(f"Awesome! 5 points! Your score is now {score}.")
            else:
                print(f"Incorrect again! 0 points this round")

        i += 1
    return score
s = quiz()
    
def goodbye(final_score, name):
        if final_score == 50:
            print(f"\n\nCongratulations {name}! You got a perfect score of {final_score}!")
        else:
            print(f"\n\nFinal score: {final_score}.")
        print("Thanks for playing the NYG Trivia Game!  Goodbye!")

goodbye(s, n)






    

     







