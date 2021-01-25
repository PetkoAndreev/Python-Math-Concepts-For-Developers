input_number = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                print_num = str(i)+str(j)+str(k)+str(l)
                sum_left_pos = 0
                sum_right_pos = 0
                curr_num = int(print_num)
                for position in range(1, 5):
                    digit = curr_num % 10
                    if curr_num > 100:
                        sum_left_pos += digit
                    else:
                        sum_right_pos += digit
                    curr_num //= 10
                if sum_left_pos == sum_right_pos and input_number % sum_left_pos == 0:
                    print(print_num, end = ' ')