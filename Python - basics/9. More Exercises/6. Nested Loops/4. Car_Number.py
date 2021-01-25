num_start = int(input())
num_end = int(input())

for first_num in range(num_start, num_end + 1):
    for second_num in range(num_start, num_end + 1):
        for third_num in range(num_start, num_end + 1):
            for fourth_num in range(num_start, num_end + 1):
                if first_num > fourth_num and (second_num + third_num) % 2 == 0 and ((first_num % 2 == 0 and fourth_num % 2 != 0) or (first_num % 2 != 0 and fourth_num % 2 == 0)):
                    print(f'{first_num}{second_num}{third_num}{fourth_num}', end = ' ')