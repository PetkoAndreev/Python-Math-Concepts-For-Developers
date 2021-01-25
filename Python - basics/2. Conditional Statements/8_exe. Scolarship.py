import math
income = float(input())
avg_success = float(input())
min_salary = float(input())

if avg_success > 4.5:
    if avg_success < 5.5:
        if income >= min_salary:
            print('You cannot get a scholarship!')
        else:
            print(f'You get a Social scholarship {math.floor(0.35 * min_salary)} BGN')
    else:
        if income < min_salary:
            if 0.35 * min_salary <= 25*avg_success:
                print(f'You get a scholarship for excellent results {math.floor(25*avg_success)} BGN')
            else:
                print(f'You get a Social scholarship {math.floor(0.35 * min_salary)} BGN')
        else:
            print(f'You get a scholarship for excellent results {math.floor(25 * avg_success)} BGN')
else:
    print('You cannot get a scholarship!')