type_flowers = input()
number_flowers = int(input())
budget = float(input())

if type_flowers == 'Roses' and number_flowers > 80:
    price = number_flowers * 5 - 0.1*(number_flowers * 5)
    if price <= budget:
        print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {budget - price:.2f} leva left.')
    else:
        print(f'Not enough money, you need {price - budget:.2f} leva more.')
elif type_flowers == 'Roses' and number_flowers <= 80:
    price = number_flowers * 5
    if price <= budget:
        print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {budget - price:.2f} leva left.')
    else:
        print(f'Not enough money, you need {price - budget:.2f} leva more.')

elif type_flowers == 'Dahlias' and number_flowers > 90:
    price = number_flowers * 3.8 - 0.15*(number_flowers * 3.8)
    if price <= budget:
        print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {budget - price:.2f} leva left.')
    else:
        print(f'Not enough money, you need {price - budget:.2f} leva more.')
elif type_flowers == 'Dahlias' and number_flowers <= 90:
    price = number_flowers * 3.8
    if price <= budget:
        print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {budget - price:.2f} leva left.')
    else:
        print(f'Not enough money, you need {price - budget:.2f} leva more.')

elif type_flowers == 'Tulips' and number_flowers > 80:
    price = number_flowers * 2.8 - 0.15*(number_flowers * 2.8)
    if price <= budget:
        print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {budget - price:.2f} leva left.')
    else:
        print(f'Not enough money, you need {price - budget:.2f} leva more.')
elif type_flowers == 'Tulips' and number_flowers <= 80:
    price = number_flowers * 2.8
    if price <= budget:
        print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {budget - price:.2f} leva left.')
    else:
        print(f'Not enough money, you need {price - budget:.2f} leva more.')

elif type_flowers == 'Narcissus' and number_flowers < 120:
    price = number_flowers * 3 + 0.15*(number_flowers * 3)
    if price <= budget:
        print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {budget - price:.2f} leva left.')
    else:
        print(f'Not enough money, you need {price - budget:.2f} leva more.')
elif type_flowers == 'Narcissus' and number_flowers >= 120:
    price = number_flowers * 3
    if price <= budget:
        print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {budget - price:.2f} leva left.')
    else:
        print(f'Not enough money, you need {price - budget:.2f} leva more.')

elif type_flowers == 'Gladiolus' and number_flowers < 80:
    price = number_flowers * 2.5 + 0.2*(number_flowers * 2.5)
    if price <= budget:
        print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {budget - price:.2f} leva left.')
    else:
        print(f'Not enough money, you need {price - budget:.2f} leva more.')
elif type_flowers == 'Gladiolus' and number_flowers >= 80:
    price = number_flowers * 2.5
    if price <= budget:
        print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {budget - price:.2f} leva left.')
    else:
        print(f'Not enough money, you need {price - budget:.2f} leva more.')