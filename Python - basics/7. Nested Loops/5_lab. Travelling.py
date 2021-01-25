destination = input()
current_money = 0

while destination != 'End':
    vacation_money = float(input())
    while current_money < vacation_money:
        work_money = float(input())
        current_money += work_money
    print(f'Going to {destination}!')
    current_money = 0
    destination = input()