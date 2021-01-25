interval_start = int(input())
interval_end = int(input())
magic_number = int(input())
flag = False
combination = 0

for i in range(interval_start, interval_end + 1):
    for j in range(interval_start, interval_end + 1):
        combination += 1
        if i + j == magic_number:
            flag = True
            print(f'Combination N:{combination} ({i} + {j} = {magic_number})')
            break
    if flag:
        break
if not flag:
    print(f'{combination} combinations - neither equals {magic_number}')