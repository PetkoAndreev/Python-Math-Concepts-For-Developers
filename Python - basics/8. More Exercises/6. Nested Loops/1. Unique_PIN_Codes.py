f_num_max = int(input())
s_num_max = int(input())
t_num_max = int(input())

for first_num in range (1, f_num_max + 1):
    for second_num in range(1, s_num_max + 1):
        for third_num in range(1, t_num_max + 1):
            if first_num % 2 == 0 and second_num > 1 and third_num % 2 == 0:
                for i in range(2, second_num):
                    if (second_num % i) == 0:
                        break
                else:
                    print(f'{first_num} {second_num} {third_num}')