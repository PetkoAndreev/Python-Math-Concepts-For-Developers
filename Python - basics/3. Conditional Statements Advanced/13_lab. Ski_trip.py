days = int(input())
type_room = input()
grade = input()
nights = days - 1
if type_room == 'room for one person' and grade == 'positive':
    price = nights * 18
    price += price * 0.25
    print(f'{price:.2f}')
elif type_room == 'room for one person' and grade =='negative':
    price = nights * 18
    price -= price * 0.1
    print(f'{price:.2f}')
elif type_room == 'apartment' and grade == 'positive':
    if nights < 10:
        price = nights * 25
        price -= price * 0.3
        price += price * 0.25
        print(f'{price:.2f}')
    elif 10 <= nights <= 15:
        price = nights * 25
        price -= price * 0.35
        price += price * 0.25
        print(f'{price:.2f}')
    elif nights > 15:
        price = nights * 25
        price -= price * 0.5
        price += price * 0.25
        print(f'{price:.2f}')
elif type_room == 'apartment' and grade == 'negative':
    if nights < 10:
        price = nights * 25
        price -= price * 0.3
        price -= price * 0.1
        print(f'{price:.2f}')
    elif 10 <= nights <= 15:
        price = nights * 25
        price -= price * 0.35
        price -= price * 0.1
        print(f'{price:.2f}')
    elif nights > 15:
        price = nights * 25
        price -= price * 0.5
        price -= price * 0.1
        print(f'{price:.2f}')
elif type_room == 'president apartment' and grade == 'positive':
    if nights < 10:
        price = nights * 35
        price -= price * 0.1
        price += price * 0.25
        print(f'{price:.2f}')
    elif 10 <= nights <= 15:
        price = nights * 25
        price -= price * 0.15
        price += price * 0.25
        print(f'{price:.2f}')
    elif nights > 15:
        price = nights * 35
        price -= price * 0.2
        price += price * 0.25
        print(f'{price:.2f}')
elif type_room == 'president apartment' and grade == 'negative':
    if nights < 10:
        price = nights * 35
        price -= price * 0.1
        price -= price * 0.1
        print(f'{price:.2f}')
    elif 10 <= nights <= 15:
        price = nights * 25
        price -= price * 0.15
        price -= price * 0.1
        print(f'{price:.2f}')
    elif nights > 15:
        price = nights * 35
        price -= price * 0.2
        price -= price * 0.1
        print(f'{price:.2f}')