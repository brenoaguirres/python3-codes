def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = "paper"
    ch = {"player": player_choice, "computer": computer_choice}

    return ch


def greeting():
    return "Hello World"


response = greeting()
print(response)

choices = get_choices()
print("\n\n")
print(choices)
print("\n\n")
print(choices["player"])
print(choices["computer"])

d = {"name": "breno", "color": "blue"}


