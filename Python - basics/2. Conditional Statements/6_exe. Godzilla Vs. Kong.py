film_budget = float(input())
statists = int(input())
dress = float(input())

decor_price = 0.1*film_budget
if statists > 150:
    dress_price = (statists*dress) - 0.1*(statists*dress)
else:
    dress_price = statists*dress
if decor_price + dress_price > film_budget:
    print('Not enough money!')
    print(f'Wingard needs{(dress_price + decor_price) - film_budget: .2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with{film_budget - (dress_price + decor_price): .2f} leva left.')