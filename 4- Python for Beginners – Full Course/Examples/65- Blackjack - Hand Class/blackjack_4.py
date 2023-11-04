import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"


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
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        draw = []
        for i in range(number):
            if len(self.cards) > 1:
                draw.append(self.cards.pop())
        return draw


class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)  # extend function appends iterable items to this

    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            self.value += int(card.rank["value"])
            if card.rank["rank"] == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21

    def display(self, show_all_dealer_cards=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
                    and not show_all_dealer_cards and not self.is_blackjack():
                print("Hidden")
            else:
                print(card)

        if not self.dealer:
            print("Value:", self.get_value())
        print()


deck = Deck()
deck.shuffle()

hand = Hand()
hand.add_card(deck.deal(2))
hand.display()


