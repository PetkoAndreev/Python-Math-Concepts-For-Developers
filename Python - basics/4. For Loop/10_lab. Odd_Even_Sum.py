n = int(input())
even_sum = 0
odd_sum = 0
for i in range(n):
    input_number = int(input())
    if i % 2 == 0:
        even_sum += input_number
    else:
        odd_sum += input_number

if even_sum == odd_sum:
    print(f'Yes\nSum = {even_sum}')
else:
    print(f'No\nDiff = {abs(even_sum - odd_sum)}')