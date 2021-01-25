n = int(input())
left_sum = 0
right_sum = 0

for i in range(n):
    left_num = int(input())
    left_sum += left_num
for i in range(n, n+n):
    right_num = int(input())
    right_sum += right_num

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')