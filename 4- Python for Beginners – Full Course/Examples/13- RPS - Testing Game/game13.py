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
    elif player == "rock":
        if computer == "paper":
            print("Paper covers rock! You lose.")
        else:
            print("Rock smashes scissors! You win!")
    elif player == "paper":
        if computer == "scissors":
            print("Scissors cuts paper! You lose.")
        else:
            print("Paper covers rock! You win!")
    else:
        if computer == "rock":
            print("Rock smashes scissors! You lose.")
        else:
            print("Scissors cuts paper! You win!")


while True:
    choices = get_choices()
    if choices["player"] == "quit":
        break
    check_win(choices["player"], choices["computer"])


