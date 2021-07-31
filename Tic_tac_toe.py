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


def tic_tac_toe():    
    intro()
    values = clear_playing_field()
    print_playing_field(values)
    player = 'X'
    is_filled = False
    while is_filled == False:
        index = valid_move(player, values)
        values[index] = player
        print_playing_field(values)
        is_winner = has_player_won(player, values)
        if is_winner == True:
                victory(player)
                break
        is_filled = is_field_full(values)
        player = select_next_player(player)
    else:
        print(
            "It's a tie.".center(len(separator))
            )


def intro():
    print(
        "\n Hello, let's play Tic tac toe!",
      rules_head.center(len(separator)),  rules,  sep='\n'+separator+'\n'
      )  


def print_playing_field(values):

    line = '+---+---+---+'.center(len(separator))

    print(
        separator, line,
        f'| {values[0]} | {values[1]} | {values[2]} |'.center(len(separator)),
        line,
        f'| {values[3]} | {values[4]} | {values[5]} |'.center(len(separator)),
        line,
        f'| {values[6]} | {values[7]} | {values[8]} |'.center(len(separator)),
        line, separator, sep = "\n")

def clear_playing_field():
    return [' '] * 9


def valid_move(player, values):
    while True:
        move = input(f'Player {player}: Please enter your move number: ')
        if not move.isnumeric():
            print('Input is not a number.')
            continue
        else:
            x =int(move)-1

        if x not in list(range(0,9)):
            print(
                'The number is out of range. Choose a number between 1 and 9.')
            continue
        elif 'X' in values[x] or 'O' in values[x]:
            print('This field is already taken.')
            continue
        else:
            break
    return x


def has_player_won(player, values):
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
            
            
def is_field_full(values):
    emty_fields = ''.join(values).count(' ')
    if emty_fields == 0:
        return True
    else:
        return False


def select_next_player(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player


def victory(player):
    print(
        f'Player {player} won, congratulations!'
        .center(len(separator)),
        '\n'+separator
        )


tic_tac_toe()



