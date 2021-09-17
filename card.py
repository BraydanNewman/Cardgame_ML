class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
        self.visible = False

    def card_visible(self):
        self.visible = True

    def __str__(self):
        if self.visible:
            return f"{self.value}|{self.suit}"
        else:
            return f"#|#"
