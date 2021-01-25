days_count = int(input())
hours_count = int(input())
parking_price = 0

for day in range (1, days_count + 1):
    day_price = 0
    for hour in range(1, hours_count + 1):
        if day % 2 == 0 and hour % 2 != 0:
            parking_price += 2.5
            day_price += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            parking_price += 1.25
            day_price += 1.25
        else:
            parking_price += 1
            day_price += 1
    print(f'Day: {day} - {day_price:.2f} leva')
print(f'Total: {parking_price:.2f} leva')