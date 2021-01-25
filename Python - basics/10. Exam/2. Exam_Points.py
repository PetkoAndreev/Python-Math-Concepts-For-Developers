task = int(input())
points = int(input())
course = input()

if task == 1:
    if course == 'Basics':
        points = points * 0.08 - (0.2 * (points * 0.08))
    elif course == 'Fundamentals':
        points = points * 0.11
    elif course == 'Advanced':
        points = points * 0.14 + (0.2 * (points * 0.14))

elif task == 2:
    if course == 'Basics':
        points = points * 0.09
    elif course == 'Fundamentals':
        points = points * 0.11
    elif course == 'Advanced':
        points = points * 0.14 + (0.2 * (points * 0.14))

elif task == 3:
    if course == 'Basics':
        points = points * 0.09
    elif course == 'Fundamentals':
        points = points * 0.12
    elif course == 'Advanced':
        points = points * 0.15 + (0.2 * (points * 0.15))

elif task == 4:
    if course == 'Basics':
        points = points * 0.10
    elif course == 'Fundamentals':
        points = points * 0.13
    elif course == 'Advanced':
        points = points * 0.16 + (0.2 * (points * 0.16))
print(f'Total points: {points:.2f}')