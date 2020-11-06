""" A game of Tic Tac Toe """

from os import system

EMPTY = " "

PLAYER_SYMBOL = {0: "O", 1: "X"}

def display_board(pad):
    """ Display the game board

    Args:
        pad: dict - the current game board state

    Returns:
        None
    """

    system("clear")  # clear screen before new output

    print(f'|  {pad[1]}  |  {pad[2]}  |  {pad[3]}  |')
    print('|-----+-----+-----|')
    print(f'|  {pad[4]}  |  {pad[5]}  |  {pad[6]}  |')
    print('|-----+-----+-----|')
    print(f'|  {pad[7]}  |  {pad[8]}  |  {pad[9]}  |\n')


def ask_starting_player():
    """ Ask which player between X and O goes first

    Returns:
        None
    """
    while True:
        player = input('First player, which symbol do you want? (X/O): ')
        if player == 'X' or player == 'x':
            print('Starting player is X\n')
            turn = 1
            return turn
        elif player == 'O' or player == 'o':
            print('Starting player is O\n')
            turn = 0
            return turn
        else:
            print('ERROR: invalid player\n')


def ask_position(pad, turn):
    """ Ask where to put the symbol and check if that position is avaiable

    Args:
        pad: dict - current game board state

    Returns:
        pos: the position if it is valid
    """

    while True:
        pos = input(f'{PLAYER_SYMBOL[turn]} turn, Where do you want to put your symbol?: ')

        try:
            pos = int(pos)  # check if input is an integer

            # check if the input is a pad position
            if pos in range(1, 10):
                # check if the pad position is EMPTY
                if pad[pos] == EMPTY:
                    return pos
                else:
                    print('ERROR: position already occupied. Choose an empty position.')
            else:
                print('ERROR: invalid position. Choose a position between 1-9')

        except ValueError:
            print('ERROR: invalid input. Insert a positive integer')


def switch_player(turn, turn_counter):
    """ Switch the active plyer and increase the turn number

    Args:
        turn: int - active player's turn inidcator
        turn_counter: int - number of turns that have been played

    Returns:
        int: the next player turn indicator
        int: the current turn number
    """

    turn = (turn + 1) % 2
    turn_counter += 1

    return turn, turn_counter


def check_victory(pad):
    """ Check if the board state is a victory

    Args:
        pad: dict - current game board state

    Returns:
        bool: whether is a victory or not
    """

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
    """ Game Loop

    Returns:
        None
    """

    turn_counter = 0

    # empty the pad at the start of the game
    pad = {1: EMPTY, 2: EMPTY, 3: EMPTY, 4: EMPTY, 5: EMPTY, 6: EMPTY, 7: EMPTY, 8: EMPTY, 9: EMPTY}

    # turns: 0 = O, 1 = X
    turn = ask_starting_player()
    display_board(pad)

    # game loop
    while True:
        pos = ask_position(pad, turn)
        if turn == 0:
            pad[pos] = PLAYER_SYMBOL[turn]
        elif turn == 1:
            pad[pos] = PLAYER_SYMBOL[turn]

        display_board(pad)

        # check victory
        is_victory = check_victory(pad)
        if turn_counter == 9 and not is_victory:
            print("---It's a tie!---".upper())
            break
        elif is_victory:
            print(f"---{PLAYER_SYMBOL[turn]} won!---".upper())
            break

        turn, turn_counter = switch_player(turn, turn_counter)  # update turn info 


if __name__ == "__main__":
    game()
