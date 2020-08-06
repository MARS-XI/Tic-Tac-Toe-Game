""" A game of Tic Tac Toe """

EMPTY = " "


def display_board(pad):
    print(f'|  {pad[1]}  |  {pad[2]}  |  {pad[3]}  |')
    print('|-----+-----+-----|')
    print(f'|  {pad[4]}  |  {pad[5]}  |  {pad[6]}  |')
    print('|-----+-----+-----|')
    print(f'|  {pad[7]}  |  {pad[8]}  |  {pad[9]}  |\n')


def put_x(pad, pad_pos):
    pad[pad_pos] = 'X'
    return pad


def put_0(pad, pad_pos):
    pad[pad_pos] = '0'
    return pad


# ask which player between X and O goes first
def ask_starting_player():
    print('First player decides which symbol to use.')
    while True:
        player = input('Which symbol do you want? (X/O): ')
        if player == 'X' or player == 'x':
            print('Starting player is X\n')
            turn = 1
            return turn
        elif player == 'O' or player == 'o':
            print('Starting player is O\n')
            turn = 0
            return turn
        else:
            print('ERROE: player non valido\n')


# asks where to put the symbol and check if that position is avaiable
def ask_position(pad):
    while True:
        pos = input('Where do you want to put your symbol?: ')

        try:
            pos = int(pos)  # check if input is an integer

            # check if the input is a pad position
            if pos in range(1, 10):
                # check if the pad position is EMPTY
                if pad[pos] == EMPTY:
                    return pos
                else:
                    print('ERROE: posizione già occupata')
                    print('inserisci il tuo simbolo in un altra posizione vuota\n')
            else:
                print('ERROE: posizione non valida')
                print('inserisci una posizione compresa tra 1-9\n')

        except ValueError:
            print('ERROE: input non valido')
            print('inserisci una numero intero\n')


def switch_player(turn, turn_counter):
    if turn == 0:
        turn = 1
    elif turn == 1:
        turn = 0
    turn_counter += 1
    return turn, turn_counter


def check_victory(pad):
    # victory cases: 123, 456, 789, 147, 258, 369, 159, 753
    is_victory = False

    if pad[1] == pad[2] == pad[3] != EMPTY:
        is_victory = True
    elif pad[4] == pad[5] == pad[6] != EMPTY:
        is_victory = True
    elif pad[7] == pad[8] == pad[9] != EMPTY:
        is_victory = True
    elif pad[1] == pad[4] == pad[7] != EMPTY:
        is_victory = True
    elif pad[2] == pad[5] == pad[8] != EMPTY:
        is_victory = True
    elif pad[3] == pad[6] == pad[9] != EMPTY:
        is_victory = True
    elif pad[1] == pad[5] == pad[9] != EMPTY:
        is_victory = True
    elif pad[7] == pad[5] == pad[3] != EMPTY:
        is_victory = True
    elif pad[1] == pad[2] == pad[3] != EMPTY:
        is_victory = True
    return is_victory


def game():
    turn_counter = 0

    # empty the pad at the start of the game
    pad = {1: EMPTY, 2: EMPTY, 3: EMPTY, 4: EMPTY, 5: EMPTY, 6: EMPTY, 7: EMPTY, 8: EMPTY, 9: EMPTY}

    # turns: 0 = O, 1 = X
    turn = ask_starting_player()
    display_board(pad)

    # game loop
    while True:
        pos = ask_position(pad)
        if turn == 0:
            pad = put_0(pad, pos)
        elif turn == 1:
            pad = put_x(pad, pos)

        display_board(pad)

        turn, turn_counter = switch_player(turn, turn_counter)  # update turn info

        # check victory
        is_victory = check_victory(pad)
        if turn_counter == 9 and not is_victory:
            print("---It's a tie!---".upper())
            break
        elif is_victory:
            print("---You won!---".upper())
            break


if __name__ == "__main__":
    game()
