type_flower = input()
flower_number = int(input())
season = input()

if type_flower == 'Sunflower':
    if season == 'Spring':
        total_honey = flower_number * 10
    elif season == 'Summer':
        total_honey = (flower_number * 8) + 0.1 * (flower_number * 8)
    else:
        total_honey = (flower_number * 12) - 0.05 * (flower_number * 12)

elif type_flower == 'Daisy':
    if season == 'Spring':
        total_honey = (flower_number * 12) + 0.1 * (flower_number * 12)
    elif season == 'Summer':
        total_honey = (flower_number * 8) + 0.1 * (flower_number * 8)
    else:
        total_honey = (flower_number * 6) - 0.05 * (flower_number * 6)

elif type_flower == 'Lavender':
    if season == 'Spring':
        total_honey = flower_number * 12
    elif season == 'Summer':
        total_honey = (flower_number * 8) + 0.1 * (flower_number * 8)
    else:
        total_honey = (flower_number * 6) - 0.05 * (flower_number * 6)

else:
    if season == 'Spring':
        total_honey = (flower_number * 10) + 0.1 * (flower_number * 10)
    elif season == 'Summer':
        total_honey = (flower_number * 12) + 0.1 * (flower_number * 12)
    else:
        total_honey = (flower_number * 6) - 0.05 * (flower_number * 6)

print(f'Total honey harvested: {total_honey:.2f}')