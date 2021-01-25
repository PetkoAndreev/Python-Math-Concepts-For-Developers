input_num = input()
sum_prime = 0
sum_not_prime = 0
flag_prime = True

while input_num != 'stop':
    input_num = int(input_num)
    counter = 0
    if input_num < 0:
        print('Number is negative.')
    for i in range(2, input_num + 1):
        if input_num % i == 0:
            counter += 1
    if counter == 1:
        sum_prime += input_num
    elif counter > 1:
        sum_not_prime += input_num
    input_num = input()
print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_not_prime}')