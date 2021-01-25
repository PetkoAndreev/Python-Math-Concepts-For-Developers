month = input()
nbr_nights = float(input())

if month in('May', 'October'):
    price_apartment = 65 * nbr_nights
    price_studio = 50 * nbr_nights
    if 7 < nbr_nights <= 14:
        price_studio -= price_studio * 0.05
    elif nbr_nights > 14:
        price_apartment -= price_apartment * 0.1
        price_studio -= price_studio * 0.3
elif month in('June', 'September'):
    price_apartment = 68.7 * nbr_nights
    price_studio = 75.2 * nbr_nights
    if nbr_nights > 14:
        price_apartment -= price_apartment * 0.1
        price_studio -= price_studio * 0.2
elif month in('July', 'August'):
    price_apartment = 77 * nbr_nights
    price_studio = 76 * nbr_nights
    if nbr_nights > 14:
        price_apartment -= price_apartment * 0.1

print(f'Apartment: {price_apartment:.2f} lv.')
print(f'Studio: {price_studio:.2f} lv.')
