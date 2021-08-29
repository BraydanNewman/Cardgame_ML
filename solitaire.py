import random


# Card suits: Diamond = 1, Club = 2, Heart = 3, Spades = 4
# Red = Odd, Black = Even
CARD_SUITS = [1, 2, 3, 4]
DRAW_AMOUNT = 3


class SolitaireGame:
    def __init__(self):
        self.full_game_board = [[], [], [], [], [], [], []]
        self.visible_game_board = [[], [], [], [], [], [], []]
        self.foundation = [[0, 1], [0, 2], [0, 3], [0, 4]]
        self.draw_pile = []
        self.visible_3_draw = []
        self.already_drawn_pile = []

        self.game_score = 0

    def new_game(self):
        cards = []
        for i in range(len(CARD_SUITS)):
            for j in range(13):
                cards.append([j+1, i+1])
        random.shuffle(cards)

        for i in range(len(self.full_game_board)+1):
            for j in range(i):
                self.full_game_board[j].append(cards[i+j])
                cards.pop(i+j)


    def move_cards(self, from_card, to_coloumn):
        pass
