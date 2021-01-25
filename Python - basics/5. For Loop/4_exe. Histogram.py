n = int(input())
p1_numbers = 0
p2_numbers = 0
p3_numbers = 0
p4_numbers = 0
p5_numbers = 0

for i in range(n):
    num = int(input())
    if num < 200:
        p1_numbers += 1
    elif 200 <= num <= 399:
        p2_numbers += 1
    elif 400 <= num <= 599:
        p3_numbers += 1
    elif 600 <= num <= 799:
        p4_numbers += 1
    elif num >= 800:
        p5_numbers += 1

p1_perc = p1_numbers / n * 100
p2_perc = p2_numbers / n * 100
p3_perc = p3_numbers / n * 100
p4_perc = p4_numbers / n * 100
p5_perc = p5_numbers / n * 100

print(f'{p1_perc:.2f}%')
print(f'{p2_perc:.2f}%')
print(f'{p3_perc:.2f}%')
print(f'{p4_perc:.2f}%')
print(f'{p5_perc:.2f}%')
