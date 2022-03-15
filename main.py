import solitaire

base_menu = """
1. (D)raw
2. (M)ove
3. (S)ave
3. (Q)uit
"""

from_move_menu = """
From Which Position:
1. (B)oard
2. (F)oundation
3. (D)eck
"""

to_move_menu = """
To Which Position:
1. (B)oard
2. (F)oundation
"""


def main():
    game = solitaire.SolitaireGame()
    game.new_game()

    while not game.win:
        print("\n")
        game.print_game()
        print(base_menu)
        choice = input(">>> ").upper()

        if choice == "D":
            game.draw()

        elif choice == "M":
            game.move_cards(move_inputs())

        elif choice == "S":
            pass

        elif choice == "Q":
            exit()

        else:
            print("Invalid Choice")


def move_inputs():
    valid_input = False
    from_move_pos = {}
    to_move_pos = {}

    while not valid_input:
        print(from_move_menu)
        from_choice = input(">>> ").upper()

        if from_choice == "B":
            valid_input = True

            x = int(input("Column of Card: "))
            y = int(input("Row of Card"))

            from_move_pos["place"] = "B"
            from_move_pos["x"] = x
            from_move_pos["y"] = y

        elif from_choice == "F":
            valid_input = True
            x = int(input("Foundation Number: "))

            from_move_pos["place"] = "F"
            from_move_pos["x"] = x

        elif from_choice == "D":
            valid_input = True
            from_move_pos["place"] = "D"

        else:
            print("Invalid Choice")

    valid_input = False
    while not valid_input:
        print(to_move_menu)
        from_choice = input(">>> ").upper()

        if from_choice == "B":
            valid_input = True

            x = int(input("Column of Cards: "))

            to_move_pos["place"] = "B"
            to_move_pos["x"] = x

        elif from_choice == "F":
            valid_input = True
            to_move_pos["place"] = "F"

        else:
            print("Invalid Choice")

    return {
        "from": from_move_pos,
        "to": to_move_pos
    }


if __name__ == "__main__":
    main()
