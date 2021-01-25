count_numbers = int(input())
p2_nums = 0
p3_nums = 0
p4_nums = 0

for i in range (1, count_numbers + 1):
    current_number = int(input())
    if current_number % 2 == 0:
        p2_nums += 1
    if current_number % 3 == 0:
        p3_nums += 1
    if current_number % 4 == 0:
        p4_nums += 1
print(f'{((p2_nums / count_numbers) * 100):.2f}%')
print(f'{((p3_nums / count_numbers) * 100):.2f}%')
print(f'{((p4_nums / count_numbers) * 100):.2f}%')