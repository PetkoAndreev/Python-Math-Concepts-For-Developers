intelligence = int(input())
power = int(input())
gender = input()

if intelligence >= 80 and power >= 80 and gender == 'female':
    print('Queen Bee')
elif intelligence >= 80:
    print('Repairing Bee')
elif intelligence >= 60:
    print('Cleaning Bee')
elif power >= 80 and gender == 'male':
    print('Drone Bee')
elif power >= 60:
    print('Guard Bee')
else:
    print('Worker Bee')