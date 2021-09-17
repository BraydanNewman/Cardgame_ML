import random
from card import Card

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
        for i in range(4):
            for j in range(13):
                cards.append(Card(j + 1, i + 1))
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
            self.already_drawn_pile += self.visible_3_draw[3:]
            del self.visible_3_draw[3:]

    def print_game(self):
        for i in self.foundation:
            print(f"{i[0]}|{i[1]}  ", end="")

        print("\t", end="")

        for i, card in enumerate(self.visible_3_draw):
            if i == 0:
                print(f"[{card}]  ", end="")
            else:
                print(f"{card}  ", end="")

        print("\n")

        max_length = len(max(self.full_game_board, key=len))

        print("     1    2    3    4    5    6    7 ")

        for i in range(max_length):
            print(f"{i + 1:2}", end="")
            for j in range(7):
                try:
                    print(f"{str(self.full_game_board[j][i]):>5}", end="")
                except IndexError:
                    print(f"{'':5}", end="")
            print("")

    def update_visible_board(self):
        for i in range(len(self.full_game_board)):
            self.full_game_board[i][-1].card_visible()

    def move_cards(self, from_card_pos, to_column):
        if to_column == "f":
            pass
        else:
            from_card = self.full_game_board[int(from_card_pos[0]) - 1][int(from_card_pos[1]) - 1]
            to_card = self.full_game_board[int(to_column) - 1][-1]

            if from_card.visible:
                from_colour_black = False
                if from_card.suit % 2 == 0:
                    from_colour_black = True

                to_colour_black = False
                if to_card.suit % 2 == 0:
                    to_colour_black = True

                if not from_colour_black == to_colour_black:
                    if to_card.value - 1 == from_card.value:
                        print("Success")

                        self.full_game_board[int(to_column) - 1] += (self.full_game_board[int(from_card_pos[0]) - 1][int(from_card_pos[1]) - 1:])

                        del self.full_game_board[int(from_card_pos[0]) - 1][int(from_card_pos[1]) - 1:]

                    self.update_visible_board()

                else:
                    print("Cards Can't be the same colour")
            else:
                print("Card Can Not be moved")
