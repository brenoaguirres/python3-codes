import random


def get_choices():
    options = ["rock", "scissors", "paper"]

    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices


def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}...")
    if player == computer:
        print("It's a tie!")


check_win("rock", "paper")

name = "Breno"
age = 25
print(f"{name} is {25} years old.")

