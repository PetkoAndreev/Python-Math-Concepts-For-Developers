n = int(input())
p1_numbers = 0
p2_numbers = 0
p3_numbers = 0

for i in range(1, n + 1):
    num = int(input())
    if num % 2 == 0:
        p1_numbers += 1
    if num % 3 == 0:
        p2_numbers += 1
    if num % 4 == 0:
        p3_numbers += 1

p1_perc = p1_numbers / n * 100
p2_perc = p2_numbers / n * 100
p3_perc = p3_numbers / n * 100

print(f'{p1_perc:.2f}%')
print(f'{p2_perc:.2f}%')
print(f'{p3_perc:.2f}%')
