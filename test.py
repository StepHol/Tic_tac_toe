separator =  "=" * 40
line = '+---+---+---+'.center(len(separator))




def clear_playing_field():
    return [' '] * 9

def print_playing_field(values):
    print(
    separator, line,
    f'| {values[0]} | {values[1]} | {values[2]} |'.center(len(separator)),
    line,
    f'| {values[3]} | {values[4]} | {values[5]} |'.center(len(separator)),
    line,
    f'| {values[6]} | {values[7]} | {values[8]} |'.center(len(separator)),
    line, separator, sep = "\n")


values = clear_playing_field()

print_playing_field(values)