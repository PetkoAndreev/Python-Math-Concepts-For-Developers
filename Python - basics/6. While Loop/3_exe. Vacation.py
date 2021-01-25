vacation_money = float(input())
current_money = float(input())
days_counter = 0
spend_days = 0

while current_money < vacation_money and spend_days < 5:
    type_action = input()
    daily_money = float(input())
    if type_action == 'spend' and daily_money >= current_money:
        current_money = 0
        spend_days += 1
    elif type_action == 'spend' and daily_money < current_money:
        current_money -= daily_money
        spend_days += 1
    else:
        current_money += daily_money
        spend_days = 0
    days_counter += 1

if spend_days == 5:
    print(f'You can\'t save the money.\n{days_counter}')

if current_money >= vacation_money:
    print(f'You saved the money for {days_counter} days.')
