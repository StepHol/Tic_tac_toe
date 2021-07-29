'''
author = Štěpán Holub
'''

rules = '''
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
'''


def tic_tac_toe():    
    intro()
    values = clear_playing_field()
    print_playing_field(values)
    player = 'X'
    flag_game_active = True
    while flag_game_active == True:
        index = execute_move(player, values)
        values[index] = player
        print_playing_field(values)
        flag_game_active = game_active(player, values)
        player = select_next_player(player)

def intro():
    print("Hello, let's play Tic tac toe!")  
    print(rules)
    

def print_playing_field(values):
    print('+---+---+---+',
    f'| {values[0]} | {values[1]} | {values[2]} |',
    '+---+---+---+',
    f'| {values[3]} | {values[4]} | {values[5]} |',
    '+---+---+---+',
    f'| {values[6]} | {values[7]} | {values[8]} |',
    '+---+---+---+', sep = "\n")

def clear_playing_field():
    return [' '] * 9


def execute_move(player, values):
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

def game_active(player, values):
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
            print(f'Player {player} won, congratulations!')
            game_active = False
            return game_active

    emty_fields = ''.join(values).count(' ')

    if emty_fields == 0:
        print("It's a tie.")
        game_active = False
        return game_active
    else:
        game_active = True
        return game_active


def select_next_player(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player

print('Game over.')

# upravit zarovnani
# (counter)

tic_tac_toe()



