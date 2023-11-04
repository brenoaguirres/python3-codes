import random


class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ["Spades", "Clubs", "Hearts", "Diamond"]
        self.ranks = [{"rank": "A", "value": 11},
                 {"rank": "2", "value": 2},
                 {"rank": "3", "value": 3},
                 {"rank": "4", "value": 4},
                 {"rank": "5", "value": 5},
                 {"rank": "6", "value": 6},
                 {"rank": "7", "value": 7},
                 {"rank": "8", "value": 8},
                 {"rank": "9", "value": 9},
                 {"rank": "10", "value": 10},
                 {"rank": "J", "value": 10},
                 {"rank": "Q", "value": 10},
                 {"rank": "K", "value": 10},
                 ]

        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append([suit, rank])

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        draw = []
        for i in range(number):
            if len(self.cards) < 1:
                draw.append(self.cards.pop())
        return draw


deck1 = Deck()
deck1.shuffle()
print(deck1.cards)
