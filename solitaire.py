import random
from card import Card

DRAW_AMOUNT = 3


class SolitaireGame:
    def __init__(self):
        self.full_game_board = [[], [], [], [], [], [], []]
        self.foundation = [[Card(0, 1, True)], [Card(0, 2, True)], [Card(0, 3, True)], [Card(0, 4, True)]]
        self.draw_pile = []
        self.visible_3_draw = []
        self.already_drawn_pile = []

        self.game_score = 0

        self.win = False

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
            print(f"{i[-1]}  ", end="")

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
            if len(self.full_game_board[i]) != 0:
                self.full_game_board[i][-1].card_visible()

    @staticmethod
    def check_valid_move(from_card, to_card, to_foundation):
        if from_card.visible:
            if to_foundation:
                if from_card.suit == to_card.suit and from_card.value - 1 == to_card.value:
                    return True
                else:
                    print("Error: Wrong Suit or Wrong Value")
                    return False

            else:
                if to_card.value == 14:
                    if from_card.value == 13:
                        return True
                    else:
                        return False
                if from_card.suit % 2 != to_card.suit % 2 and from_card.value + 1 == to_card.value:
                    return True

                else:
                    print("Error: Same Color Suit or Wrong Value")
                    return False

        else:
            print("Error: Invalid Move")
            return False

    def move_cards(self, move_pos):
        foundation_index = 0

        if move_pos['from']['place'] == "B":
            from_card = self.full_game_board[move_pos['from']['x'] - 1][move_pos['from']['y'] - 1]

            temp_cards = self.full_game_board[move_pos['from']['x'] - 1][move_pos['from']['y'] - 1:]

        elif move_pos['from']['place'] == "F":
            from_card = self.foundation[move_pos['from']['x'] - 1][-1]
            temp_cards = [from_card]

        elif move_pos['from']['place'] == "D":
            from_card = self.visible_3_draw[0]
            temp_cards = [from_card]

        else:
            print("Error")
            return

        if move_pos['from']['place'] == "B" and move_pos['to']['place'] == "F":
            if self.full_game_board[move_pos['from']['x'] - 1][-1] != from_card:
                print("Error")
                return

        to_foundation = False
        if move_pos['to']['place'] == "B":
            if len(self.full_game_board[move_pos['to']['x'] - 1]) != 0:
                to_card = self.full_game_board[move_pos['to']['x'] - 1][-1]
            else:
                to_card = Card(14, 5, True)

        elif move_pos['to']['place'] == "F":
            to_foundation = True

            for i, item in enumerate(self.foundation):
                if item[0].suit == from_card.suit:
                    foundation_index = i

            to_card = self.foundation[foundation_index][-1]

        else:
            print("Error")
            return

        if self.check_valid_move(from_card, to_card, to_foundation):
            if move_pos['from']['place'] == "B":
                del self.full_game_board[move_pos['from']['x'] - 1][move_pos['from']['y'] - 1:]

                if move_pos['to']['place'] == "B":
                    self.full_game_board[move_pos['to']['x'] - 1] += temp_cards

                else:
                    self.foundation[foundation_index] += temp_cards

            elif move_pos['from']['place'] == "F":
                del self.foundation[move_pos['from']['x'] - 1][-1]

                self.full_game_board[move_pos['to']['x'] - 1] += temp_cards

            elif move_pos['from']['place'] == "D":
                del self.visible_3_draw[0]
                if len(self.already_drawn_pile[-1]) != 0:
                    self.visible_3_draw.append(self.already_drawn_pile[-1])
                del self.already_drawn_pile[-1]

                if move_pos['to']['place'] == "B":
                    self.full_game_board[move_pos['to']['x'] - 1] += temp_cards

                else:
                    self.foundation[move_pos['to']['place'] - 1] += temp_cards

        else:
            print("Invalid Move")

        self.update_visible_board()
