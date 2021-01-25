budget = float(input())
fuel = float(input())
week_day = input()
safari_price = (fuel * 2.1) + 100
money_left_sat = budget - (safari_price - safari_price * 0.1)
money_left_sun = budget - (safari_price - safari_price * 0.2)

if week_day == 'Saturday':
    if money_left_sat >= 0:
        print(f'Safari time! Money left: {money_left_sat:.2f} lv.')
    else:
        print(f'Not enough money! Money needed: {abs(money_left_sat):.2f} lv.')
else:
    if money_left_sun >= 0:
        print(f'Safari time! Money left: {money_left_sun:.2f} lv.')
    else:
        print(f'Not enough money! Money needed: {abs(money_left_sun):.2f} lv.')

