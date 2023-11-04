def get_choices():
    player_choice = "rock"
    computer_choice = "paper"
    ch = {"player": player_choice, "computer": computer_choice}

    return ch


def greeting():
    return "Hello World"


response = greeting()
print(response)

choices = get_choices()
print(choices["player"])
print(choices["computer"])

d = {"name": "breno", "color": "blue"}


