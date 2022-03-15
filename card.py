# Card suits: Diamond = 1, Club = 2, Heart = 3, Spades = 4
# Red = Odd, Black = Even

SUIT_CONVERSION = {
    1: "D",
    2: "C",
    3: "H",
    4: "S"
}

VALUE_CONVERSION = {
    1: "A",
    11: "J",
    12: "Q",
    13: "K"
}


class Card:
    def __init__(self, value, suit, visible=False):
        self.suit = suit
        self.value = value
        self.visible = visible

    def card_visible(self):
        self.visible = True

    def __str__(self):
        if self.visible:
            suit = self.value
            value = self.value

            if self.value in VALUE_CONVERSION:
                value = VALUE_CONVERSION[self.value]

            if self.suit in SUIT_CONVERSION:
                suit = SUIT_CONVERSION[self.suit]

            return f"{value}|{suit}"
        else:

            return "#|#"
