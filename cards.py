class deck:
    suits = ["heart", "diamond", "spade", "club"]
    values = ["Ace", "Jack", "King", "Queen", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for value in self.values:
                if suit == "heart" or suit == "diamond":
                    self.cards.append(card(value, suit, "Red"))
                else:
                    self.cards.append(card(value, suit, "Black"))
    

class card:
    def __init__(self, value, suit, color):
        self.value = value
        self.suit = suit
        self.color = color

    def show(self):
        print(f"{self.color} {self.value} of {self.suit}")


deck1 = deck()