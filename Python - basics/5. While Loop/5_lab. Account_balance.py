money = input()
balance = 0
while money != 'NoMoreMoney':
    if float(money) < 0:
        print('Invalid operation!')
        break
    money = float(money)
    print(f'Increase: {money:.2f}')
    balance += money
    money = input()

print(f'Total: {balance:.2f}')