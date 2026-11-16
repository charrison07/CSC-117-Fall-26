import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(p, c):
    if p == c:
        return "tie"
    if p == "rock" and c == "scissors":
        return "player"
    if p == "paper" and c == "rock":
        return "player"
    if p == "scissors" and c == "paper":
        return "player"
    return "computer"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    score_p = 0
    score_c = 0
    rounds = 3
    i = 0
    while i < rounds:
        p = input("Enter rock, paper, or scissors: ")
        c = get_computer_choice()
        print("Computer chose: " + c)
        w = determine_winner(p, c)
        if w == "player":
            print("You win this round!")
            score_p = score_p + 1
        elif w == "computer":
            print("Computer wins this round!")
            score_c = score_c + 1
        else:
            print("It's a tie!")
        i = i + 1
    print("Final Score - You: " + str(score_p) + " Computer: " + str(score_c))

play_game()