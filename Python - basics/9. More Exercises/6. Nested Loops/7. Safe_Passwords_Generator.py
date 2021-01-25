a = int(input())
b = int(input())
max_num_passwords = int(input())
flag = False
counter = 0
letter_a = 35
letter_b = 64

for x in range(1, a + 1):
    for y in range(1, b + 1):
        print(f'{chr(letter_a)}{chr(letter_b)}{x}{y}{chr(letter_b)}{chr(letter_a)}|', end = '')
        letter_a += 1
        letter_b += 1
        if letter_a > 55:
            letter_a = 35
        if letter_b > 96:
            letter_b = 64
        counter += 1
        if counter == max_num_passwords:
            flag = True
            break
    if flag:
        break



