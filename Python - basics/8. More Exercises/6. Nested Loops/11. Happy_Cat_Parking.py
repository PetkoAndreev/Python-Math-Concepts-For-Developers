num_days = int(input())
num_hours = int(input())
total_tax = 0

for i in range(1, num_days + 1):
    tax = 0
    for j in range (1, num_hours + 1):
        if i % 2 == 0 and j % 2 != 0:
            tax += 2.5
        elif i % 2 != 0 and j % 2 == 0:
            tax += 1.25
        else:
            tax += 1
    total_tax += tax
    print(f'Day: {i} - {tax:.2f} leva')
print(f'Total: {total_tax:.2f} leva')
