def get_choices():
    player_choice = "rock"
    computer_choice = "paper"

    return player_choice, computer_choice


def greeting():
    return "Hello World"


response = greeting()
print(response)

choices = get_choices()
print(choices[0])
print(choices[1])

