lili_age = int(input())
laundry_machine = float(input())
toy_price = float(input())
number_toys = 0
money = 0
if 1 <= lili_age <= 77:
    for i in range(1, lili_age + 1):
        if i % 2 == 0:
            money += (10 * i)/2 - 1
        else:
            number_toys += 1
sum_toys = number_toys * toy_price
total_sum = money + sum_toys
if total_sum >= laundry_machine:
    print(f'Yes! {total_sum - laundry_machine:.2f}')
else:
    print(f'No! {laundry_machine - total_sum:.2f}')
