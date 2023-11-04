import random


def get_choices():
    options = ["rock", "scissors", "paper"]

    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(options)
    ch = {"player": player_choice, "computer": computer_choice}

    return ch


choices = get_choices()
print(choices)

food = ["pizza", "carrots", "eggs"]
dinner = random.choice(food)
print(dinner)

