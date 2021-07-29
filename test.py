list = ['X', 'X', 'O']

all_fields = ''.join(list)

print(all_fields)


for comb in winning_combinations:
    if comb == 3:
        print(f'Player {player} won, congratulations!')
    break