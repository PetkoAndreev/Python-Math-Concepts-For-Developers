chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

menu_price = chicken_menu * 10.35 + fish_menu * 12.4 + veggie_menu * 8.15
dessert_price = 0.2 * menu_price
total_price = menu_price + dessert_price + 2.5

print(f'Total: {total_price:.2f}')