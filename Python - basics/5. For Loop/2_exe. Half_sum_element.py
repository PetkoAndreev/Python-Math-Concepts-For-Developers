import sys
n = int(input())
max_num = -sys.maxsize
sum_numbers = 0
for i in range(n):
    num = int(input())
    sum_numbers += num
    if num > max_num:
        max_num = num

other_sum = sum_numbers - max_num

if other_sum == max_num:
    print(f'Yes\nSum = {other_sum}')
else:
    print(f'No\nDiff = {abs(max_num - other_sum)}')