day_of_week = input()
work_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
vacation_days = ['Saturday', 'Sunday']
if day_of_week in (work_days):
    print('Working day')
elif day_of_week in (vacation_days):
    print('Weekend')
else:
    print('Error')