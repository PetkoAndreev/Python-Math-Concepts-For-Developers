contract_time = input()
contract_type = input()
contract_internet = input()
months_to_pay = int(input())

if contract_time == 'one':
    if contract_type == 'Small':
        price = 9.98
    elif contract_type == 'Middle':
        price = 18.99
    elif contract_type == 'Large':
        price = 25.98
    else:
        price = 35.99
else:
    if contract_type == 'Small':
        price = 8.58
    elif contract_type == 'Middle':
        price = 17.09
    elif contract_type == 'Large':
        price = 23.59
    else:
        price = 31.79

if contract_internet == 'yes':
    if price <= 10:
        price += 5.5
    elif 10 < price <= 30:
        price += 4.35
    else:
        price += 3.85

if contract_time == 'two':
    price = price - (price * 0.0375)

print(f'{(price*months_to_pay):.2f} lv.')