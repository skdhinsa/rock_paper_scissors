import random


def user_selection():
    inputs = ["rock", "paper", "scissors"]
    user = input("Choose rock, paper, scissors? ")
    if user not in inputs:
        print("Sorry that was not a valid input. Try again: ")
        user = user_selection()
    return user


def computer_selection():
    randNum = random.randint(0, 2)
    if randNum == 0:
        return "rock"
    elif randNum == 1:
        return "paper"
    elif randNum == 2:
        return "scissors"


def determine_winner(user, comp):
    if (
        (user == "rock" and comp == "scissors")
        or (user == "scissors" and comp == "paper")
        or (user == "paper" and comp == "rock")
    ):
        print(f"{user} (you) vs {comp} (computer)")
        print("You win!")
    elif user == comp:
        print(f"{user} (you) vs {comp} (computer)")
        print("draw")
    else:
        print(f"{user} (you) vs {comp} (computer)")
        print("You lose")


def play_game():
    while True:
        user = user_selection()
        comp = computer_selection()
        determine_winner(user, comp)

        playAgain = input("Play again: y/n?")
        if playAgain != "y":
            break
