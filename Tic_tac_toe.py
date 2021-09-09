'''
author = Štěpán Holub
'''
rules_head = 'GAME RULES'

rules = '''Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row'''

separator =  "=" * 42


def tic_tac_toe() -> None:  
    '''
    The function takes inputs of moves from players 'X' and 'O' one by one 
    and assign them into 3x3 grid. If there is a row of three same marks,
    the function prints the winning player. If  there is no field feft,
    the function prints a tie statement.
    '''
    intro()
    values = clear_playing_field() 
    '''
    values: list stores actual distribution of player marks.
    Contains 9 strings that can take values
    'X', 'O' or '_' (an empty field).
    '''
    print_playing_field(values)
    player = 'X'
    while all_fields_full(values) == False:
        values[input_valid_move(player, values)] = player
        print_playing_field(values)
        if  player_is_winner(player, values) == True:
                victory(player)
                break
        player = select_next_player(player)
    else:
        print(
            "It's a tie.".center(len(separator))
            )


def intro() -> None:
    print(
        "\n Hello, let's play Tic tac toe!",
      rules_head.center(len(separator)),  rules,  sep='\n'+separator+'\n'
      )  


def print_playing_field(values: list) -> None:

    line = '+---+---+---+'.center(len(separator))

    print(
        separator, line,
        f'| {values[0]} | {values[1]} | {values[2]} |'.center(len(separator)),
        line,
        f'| {values[3]} | {values[4]} | {values[5]} |'.center(len(separator)),
        line,
        f'| {values[6]} | {values[7]} | {values[8]} |'.center(len(separator)),
        line, separator, sep = "\n")

def clear_playing_field() -> list:
    return [' '] * 9


def input_valid_move(player: str, values: list) -> int:
    while True:
        move = input(f'Player {player}: Please enter your move number: ')
        if not move.isnumeric():
            print('Input is not a number.')
            continue
        else:
            move = int(move) - 1

        if move not in list(range(0,9)):
            print(
                'The number is out of range. Choose a number between 1 and 9.')
            continue
        elif 'X' in values[move] or 'O' in values[move]:
            print('This field is already taken.')
            continue
        else:
            break
    return move


def player_is_winner(player: str, values: list) -> bool:
    row_1 = ''.join([values[0], values[1], values[2]]).count(player)
    row_2 = ''.join([values[3], values[4], values[5]]).count(player)
    row_3 = ''.join([values[6], values[7], values[8]]).count(player)

    column_1 = ''.join([values[0], values[3], values[6]]).count(player)
    column_2 = ''.join([values[1], values[4], values[7]]).count(player)
    column_3 = ''.join([values[2], values[5], values[8]]).count(player)

    diagonal_1 = ''.join([values[0], values[4], values[8]]).count(player)
    diagonal_2 = ''.join([values[6], values[4], values[2]]).count(player)

    winning_combinations = [
        row_1, row_2, row_3,
        column_1, column_2, column_3,
        diagonal_1, diagonal_2]
 
    for comb in winning_combinations:
        if comb == 3:
            return True
    else:
        return False 
            
            
def all_fields_full(values: list) -> bool:
    emty_fields = ''.join(values).count(' ')
    if emty_fields == 0:
        return True
    else:
        return False


def select_next_player(player: str) -> str:
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player


def victory(player: str) -> None:
    print(
        f'Player {player} won, congratulations!'
        .center(len(separator)),
        '\n'+separator
        )


if __name__ == "__main__":
    tic_tac_toe()



