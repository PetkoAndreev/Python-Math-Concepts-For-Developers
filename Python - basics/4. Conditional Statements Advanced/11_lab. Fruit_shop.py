fruit = input()
day_of_week = input()
quantity = float(input())
if day_of_week in('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'):
    if fruit == 'banana':
        price = 2.5*quantity
        print(f'{price:.2f}')
    elif fruit == 'apple':
        price = 1.2*quantity
        print(f'{price:.2f}')
    elif fruit == 'orange':
        price = 0.85*quantity
        print(f'{price:.2f}')
    elif fruit == 'grapefruit':
        price = 1.45*quantity
        print(f'{price:.2f}')
    elif fruit == 'kiwi':
        price = 2.7*quantity
        print(f'{price:.2f}')
    elif fruit == 'pineapple':
        price = 5.5*quantity
        print(f'{price:.2f}')
    elif fruit == 'grapes':
        price = 3.85*quantity
        print(f'{price:.2f}')
    else:
        print('error')
elif day_of_week in('Saturday', 'Sunday'):
    if fruit == 'banana':
        price = 2.7*quantity
        print(f'{price:.2f}')
    elif fruit == 'apple':
        price = 1.25*quantity
        print(f'{price:.2f}')
    elif fruit == 'orange':
        price = 0.9*quantity
        print(f'{price:.2f}')
    elif fruit == 'grapefruit':
        price = 1.6*quantity
        print(f'{price:.2f}')
    elif fruit == 'kiwi':
        price = 3*quantity
        print(f'{price:.2f}')
    elif fruit == 'pineapple':
        price = 5.6*quantity
        print(f'{price:.2f}')
    elif fruit == 'grapes':
        price = 4.2*quantity
        print(f'{price:.2f}')
    else:
        print('error')
else:
    print('error')