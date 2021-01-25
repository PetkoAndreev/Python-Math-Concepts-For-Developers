start_num = int(input())
end_num = int(input())
magic_num = int(input())
counter = 0
flag = False

for first_num in range (start_num, end_num + 1):
    for second_num in range (start_num, end_num + 1):
        counter += 1
        if first_num + second_num == magic_num:
            print(f'Combination N:{counter} ({first_num} + {second_num} = {magic_num})')
            flag = True
            break
    if flag:
        break
if not flag:
    print(f'{counter} combinations - neither equals {magic_num}')