import random


def get_choices():
    options = ["rock", "scissors", "paper"]

    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices


def check_win(player, computer):
    if player == computer:
        return "It's a tie!"


a = 3
b = 5
if a > b:
    print("Yes")


