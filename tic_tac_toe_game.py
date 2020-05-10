"""
A game of Tic Tac Toe
"""

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


# aks which player between X and O goes first
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


# asks where tu put the symbol and check if that position is avaiable
def ask_position(pad):
    while True:
        pos = input('Where do you want to put your symbol?: ')
        print()
        # checks if input is an integer
        try:
            pos = int(pos)
            # checks if the input is a pad position
            if pos in range(1, 10):
                # checks if the pad position is empty
                if pad[pos] == ' ':
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

    if pad[1] == pad[2] == pad[3] and pad[1] != ' ' and pad[2] != ' ' and pad[3] != ' ':
        is_victory = True
    elif pad[4] == pad[5] == pad[6] and pad[4] != ' ' and pad[5] != ' ' and pad[6] != ' ':
        is_victory = True
    elif pad[7] == pad[8] == pad[9] and pad[7] != ' ' and pad[8] != ' ' and pad[9] != ' ':
        is_victory = True
    elif pad[1] == pad[4] == pad[7] and pad[1] != ' ' and pad[4] != ' ' and pad[7] != ' ':
        is_victory = True
    elif pad[2] == pad[5] == pad[8] and pad[2] != ' ' and pad[5] != ' ' and pad[8] != ' ':
        is_victory = True
    elif pad[3] == pad[6] == pad[9] and pad[3] != ' ' and pad[6] != ' ' and pad[9] != ' ':
        is_victory = True
    elif pad[1] == pad[5] == pad[9] and pad[1] != ' ' and pad[5] != ' ' and pad[9] != ' ':
        is_victory = True
    elif pad[7] == pad[5] == pad[3] and pad[7] != ' ' and pad[5] != ' ' and pad[3] != ' ':
        is_victory = True
    elif pad[1] == pad[2] == pad[3] and pad[1] != ' ' and pad[2] != ' ' and pad[3] != ' ':
        is_victory = True
    return is_victory


def game():

    # starting sequence
    turn = 0  # starting turn, 0 = O, 1 = X
    turn_counter = 0
    empty = ' '
    # empties the pad at the start of the game
    pad = {1: empty, 2: empty, 3: empty, 4: empty, 5: empty, 6: empty, 7: empty, 8: empty, 9: empty}
    turn = ask_starting_player()
    display_board(pad)

    do_continue = True
    while do_continue:
        # game sequence
        pos = ask_position(pad)
        if turn == 0:
            pad = put_0(pad, pos)
        elif turn == 1:
            pad = put_x(pad, pos)
        display_board(pad)

        turn, turn_counter = switch_player(turn, turn_counter)
        # check ending sequence
        is_victory = check_victory(pad)
        if turn_counter == 9 and not is_victory:
            print("---It's a tie!---".upper())
            do_continue = False
        elif is_victory:
            print("---You won!---".upper())
            do_continue = False

if __name__ == "__main__":
    game()
