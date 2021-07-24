'''
author = Štěpán Holub
'''

print("Hello, let's play Tic tac toe!")

# vypis pravidla hry
# print hraci plochy

values = list(range(1,10))

def playing_field():
    print('+---+---+---+')
    print(f'| {values[0]} | {values[1]} | {values[2]} |')
    print('+---+---+---+')
    print(f'| {values[3]} | {values[4]} | {values[5]} |')
    print('+---+---+---+')
    print(f'| {values[6]} | {values[7]} | {values[8]} |')
    print('+---+---+---+')

def execute_move(player):
    playing_field()
    move = input(f'Player {player}: Please enter your move number: ')
    if not move.isdigit():
        print('Input is not a number.')
    else:
        x =int(move)
    if x not in list(range(1,10)):
        print('The number is out of range. Choose a number between 1 and 9.')
    else:
        values[x-1] = {player}

playing_field()
values = [' ']*9
x = 0
while True:
    execute_move('X')
    execute_move('O')


    





# while loop
# input 1. hrac, kontrola vstupu, kontrola obsazenosti, kontrola 3 v rade
# input 2. hrac, 
# print plochy

# victory/draw
# counter 




