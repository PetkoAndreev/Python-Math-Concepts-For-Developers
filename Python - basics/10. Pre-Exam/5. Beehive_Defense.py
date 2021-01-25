bee_number = int(input())
bear_health = int(input())
bear_attack = int(input())

while bee_number >= 100 and bear_health > 0:
    bee_number = bee_number - bear_attack
    if bee_number < 100:
        if bee_number >= 0:
            print(f'The bear stole the honey! Bees left {bee_number}.')
        else:
            print('The bear stole the honey! Bees left 0.')
        break
    bear_health = bear_health - (bee_number * 5)
if bee_number >= 100:
    print(f'Beehive won! Bees left {bee_number}.')