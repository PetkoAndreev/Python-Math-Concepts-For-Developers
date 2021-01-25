budget = float(input())
total_products = 0
total_price = 0

while total_price <= budget:
    product_name = input()

    if product_name == 'Stop':
        print(f'You bought {total_products} products for {total_price:.2f} leva.')
        break

    product_price = float(input())

    total_products += 1

    if total_products % 3 == 0:
        product_price = product_price / 2

    total_price += product_price

    if total_price > budget:
        print(f'You don\'t have enough money!')
        print(f'You need {(total_price - budget):.2f} leva!')