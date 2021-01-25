days = int(input())
sladkar = int(input())
cake = int(input())
gofreta = int(input())
pancake = int(input())
cake_price = cake*45
gofreta_price = gofreta*5.8
pancake_price = pancake*3.2
day_price = (cake_price + gofreta_price + pancake_price)*sladkar
total_price = days*day_price
campaign = total_price - (total_price/8)
print(campaign)