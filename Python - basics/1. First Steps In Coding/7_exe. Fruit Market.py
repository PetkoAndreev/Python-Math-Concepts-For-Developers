strawberry_price = float(input())
banana_quantity = float(input())
orange_quantity = float(input())
malini_quantity = float(input())
strawberry_quantity = float(input())
malini_price = strawberry_price/2
banana_price = malini_price - 0.8*malini_price
orange_price = malini_price - 0.4*malini_price
malini_total = malini_quantity*malini_price
strawberry_total = strawberry_quantity*strawberry_price
banana_total = banana_quantity*banana_price
orange_total = orange_quantity*orange_price
total_price = strawberry_total+malini_total+orange_total+banana_total
print(total_price)