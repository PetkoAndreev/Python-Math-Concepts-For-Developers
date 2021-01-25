budget = float(input())
season = input()

if budget <= 100 and season == 'summer':
    destination = 'Bulgaria'
    type_vacation = 'Camp'
    budget = 0.3 * budget
    print(f'Somewhere in {destination} \n {type_vacation} - {budget:.2f}')
elif 100 < budget <= 1000 and season == 'summer':
    destination = 'Balkans'
    type_vacation = 'Camp'
    budget = 0.4 * budget
    print(f'Somewhere in {destination} \n {type_vacation} - {budget:.2f}')
elif budget <= 100 and season == 'winter':
    destination = 'Bulgaria'
    type_vacation = 'Hotel'
    budget = 0.7 * budget
    print(f'Somewhere in {destination} \n {type_vacation} - {budget:.2f}')
elif 100 < budget <= 1000 and season == 'winter':
    destination = 'Balkans'
    type_vacation = 'Hotel'
    budget = 0.8 * budget
    print(f'Somewhere in {destination} \n {type_vacation} - {budget:.2f}')
elif budget > 1000 :
    destination = 'Europe'
    type_vacation = 'Hotel'
    budget = 0.9 * budget
    print(f'Somewhere in {destination} \n {type_vacation} - {budget:.2f}')