degrees = float(input())
day_time = input()

if day_time == 'Morning' and 10 <= degrees <= 18:
    outfit = 'Sweatshirt'
    shoes = 'Sneakers'
    print(f'It\'s {degrees:.0f} degrees, get your {outfit} and {shoes}.')
elif day_time == 'Morning' and 18 < degrees <= 24:
    outfit = 'Shirt'
    shoes = 'Moccasins'
    print(f'It\'s {degrees:.0f} degrees, get your {outfit} and {shoes}.')
elif day_time == 'Morning' and degrees >= 25:
    outfit = 'T-Shirt'
    shoes = 'Sandals'
    print(f'It\'s {degrees:.0f} degrees, get your {outfit} and {shoes}.')
elif day_time == 'Afternoon' and 10 <= degrees <= 18:
    outfit = 'Shirt'
    shoes = 'Moccasins'
    print(f'It\'s {degrees:.0f} degrees, get your {outfit} and {shoes}.')
elif day_time == 'Afternoon' and 18 < degrees <= 24:
    outfit = 'T-Shirt'
    shoes = 'Sandals'
    print(f'It\'s {degrees:.0f} degrees, get your {outfit} and {shoes}.')
elif day_time == 'Afternoon' and degrees >= 25:
    outfit = 'Swim Suit'
    shoes = 'Barefoot'
    print(f'It\'s {degrees:.0f} degrees, get your {outfit} and {shoes}.')
elif day_time == 'Evening' and 10 <= degrees <= 18:
    outfit = 'Shirt'
    shoes = 'Moccasins'
    print(f'It\'s {degrees:.0f} degrees, get your {outfit} and {shoes}.')
elif day_time == 'Evening' and 18 < degrees <= 24:
    outfit = 'Shirt'
    shoes = 'Moccasins'
    print(f'It\'s {degrees:.0f} degrees, get your {outfit} and {shoes}.')
elif day_time == 'Evening' and degrees >= 25:
    outfit = 'Shirt'
    shoes = 'Moccasins'
    print(f'It\'s {degrees:.0f} degrees, get your {outfit} and {shoes}.')