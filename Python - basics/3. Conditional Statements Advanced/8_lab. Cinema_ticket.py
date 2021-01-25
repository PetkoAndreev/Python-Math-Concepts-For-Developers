day_of_week = input()
if day_of_week in ('Monday', 'Tuesday', 'Friday'):
    price = 12
    print(price)
elif day_of_week in ('Wednesday', 'Thursday'):
    price = 14
    print(price)
elif day_of_week in ('Saturday', 'Sunday'):
    price = 16
    print(price)