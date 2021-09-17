import random
from card import Card

# Card suits: Diamond = 1, Club = 2, Heart = 3, Spades = 4
# Red = Odd, Black = Even
CARD_SUITS = [1, 2, 3, 4]
DRAW_AMOUNT = 3


class SolitaireGame:
    def __init__(self):
        self.full_game_board = [[], [], [], [], [], [], []]
        self.foundation = [[0, 1], [0, 2], [0, 3], [0, 4]]
        self.draw_pile = []
        self.visible_3_draw = []
        self.already_drawn_pile = []

        self.game_score = 0

    def new_game(self):
        cards = []

        # Create deck of cards
        for i in range(len(CARD_SUITS)):
            for j in range(13):
                cards.append(Card(j, i))
        random.shuffle(cards)

        # Place cards in game form
        for column in range(8):
            for place in range(column):
                self.full_game_board[column - 1].append(cards[0])
                if place == column - 1:
                    self.full_game_board[column - 1][-1].card_visible()
                cards.pop(0)

        for i in cards:
            i.card_visible()
            self.draw_pile.append(i)

    def draw(self):
        for _ in range(DRAW_AMOUNT):
            self.visible_3_draw.insert(0, self.draw_pile[0])
            self.draw_pile.pop(0)

        if len(self.visible_3_draw) > 3:
            for i in range(len(self.visible_3_draw)-3, 0, -1):
                self.already_drawn_pile += self.visible_3_draw[i + 2]
                self.visible_3_draw.pop(i + 2)

    def print_game(self):
        print(f"{self.foundation}   {[str(i) for i in self.visible_3_draw]}")

        max_length = len(max(self.full_game_board, key=len))

        for i in range(max_length):
            for j in range(7):
                try:
                    print(f"{self.full_game_board[j][i]:4}", end="")
                except IndexError:
                    print(f"{'':3}", end="")
            print("")

    def update_visible_board(self):
        pass

    def move_cards(self, from_card, to_column):
        pass
