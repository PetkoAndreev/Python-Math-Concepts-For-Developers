cake_width = int(input())
cake_length = int(input())
cake_size = cake_width * cake_length
input_pieces = input()
eated_pieces = 0

while input_pieces != 'STOP':

    input_pieces = int(input_pieces)
    eated_pieces += input_pieces
    if eated_pieces > cake_size:
        print(f'No more cake left! You need {eated_pieces - cake_size} pieces more.')
        break
    input_pieces = input()

if input_pieces == 'STOP':
    print(f'{cake_size - eated_pieces} pieces are left.')