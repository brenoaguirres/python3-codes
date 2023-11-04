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
    elif player == "rock" and computer == "scissors":
        print("Rock smashes scissors! You win!")
    elif player == "rock" and computer == "paper":
        print("Paper covers rock! You lose.")


check_win("rock", "paper")

age = 20
if age >= 18:
    print("You are an adult.")
elif age > 12:
    print("You are a teenager.")
elif age > 1:
    print("You are a child.")
else:
    print("You are a baby.")

