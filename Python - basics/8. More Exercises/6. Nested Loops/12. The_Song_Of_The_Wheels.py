magic_password = int(input())
counter = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and ((a * b) + (c * d)) ==  magic_password:
                    counter += 1
                    if counter == 4:
                        pass_found = str('Password: ') + str(a) + str(b) + str(c) + str(d)
                        print(f'{a}{b}{c}{d}', end=' ')
                    else:
                        print(f'{a}{b}{c}{d}', end = ' ')

if counter < 4:
    print(f'\nNo!')
else:
    print(f'\n{pass_found}')