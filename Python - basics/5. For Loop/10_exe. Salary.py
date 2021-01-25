n = int(input())
salary = int(input())
penalty = 0

for i in range(n):
    browser_tab = input()
    if browser_tab == 'Facebook':
        penalty += 150
    elif browser_tab == 'Instagram':
        penalty += 100
    elif browser_tab == 'Reddit':
        penalty += 50

if salary - penalty <= 0:
    print('You have lost your salary.')
else:
    print(salary - penalty)