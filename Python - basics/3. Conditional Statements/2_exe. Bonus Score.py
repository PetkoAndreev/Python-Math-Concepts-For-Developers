initial_points = int(input())

if initial_points <= 100:
    bonus = 5
elif initial_points <= 1000:
    bonus = 0.2*initial_points
else:
    bonus = 0.1*initial_points

if initial_points % 2 == 0:
    bonus = bonus + 1
elif initial_points % 10 == 5:
    bonus = bonus + 2
print(f'{bonus}')
print(f'{initial_points + bonus}')