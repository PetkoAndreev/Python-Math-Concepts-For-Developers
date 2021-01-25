group_budget = float(input())
season = input()
fishermans = int(input())

if season == 'Spring':
    price_ship = 3000
elif season in('Summer', 'Autumn'):
    price_ship = 4200
else:
    price_ship = 2600

if fishermans <= 6:
    price_ship -= 0.1 * price_ship
elif 7 <= fishermans <= 11:
    price_ship -= 0.15 * price_ship
else:
    price_ship -= 0.25 * price_ship

if fishermans % 2 == 0 and season != 'Autumn':
    price_ship -= 0.05 * price_ship

if group_budget >= price_ship:
    print(f'Yes! You have {group_budget - price_ship:.2f} leva left.')
else:
    print(f'Not enough money! You need {price_ship - group_budget:.2f} leva.')
