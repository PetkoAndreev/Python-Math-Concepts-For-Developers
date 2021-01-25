import math
student_name = input()

while student_name != 'Midnight':
    total_points = 0
    for i in range(1, 7):
        points = int(input())
        if points > 100:
            points = 100
        total_points += points
        if points < 0:
            total_points = -1
            print(f'{student_name} was cheating!')
            break
    if total_points >= 0:
        total_points = math.floor(total_points / 6)
        grade = total_points * 0.06
        if grade >= 5:
            print('===================')
            print('|   CERTIFICATE   |')
            print(f'|    {grade:.2f}/6.00    |')
            print('===================')
            print(f'Issued to {student_name}')
        elif grade < 3:
            grade = 2
            print(f'{student_name} - {grade:.2f}')
        else:
            print(f'{student_name} - {grade:.2f}')

    student_name = input()