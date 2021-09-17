import solitaire


def main():
    game = solitaire.SolitaireGame()
    game.new_game()
    game.draw()
    game.print_game()
    from_card_column = int(input('From Card Column: '))
    from_card_row = int(input('From Card Row: '))

    to_card_column = int(input("To Card Column: "))

    game.move_cards([from_card_column, from_card_row], to_card_column)

    game.print_game()


if __name__ == "__main__":
    main()
