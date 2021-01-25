screeing_type = input()
rows = int(input())
colums = int(input())

if screeing_type == 'Premiere':
    print(f'{rows * colums * 12:.2f} leva')
elif screeing_type == 'Normal':
    print(f'{rows * colums * 7.5:.2f} leva')
elif screeing_type == 'Discount':
    print(f'{rows * colums * 5:.2f} leva')