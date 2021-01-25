bees = int(input())
flowers = int(input())

total_honey = bees * flowers * 0.21
honeycombs = total_honey // 100
honey_left = total_honey % 100

print(f'{honeycombs:.0f} honeycombs filled.')
print(f'{honey_left:.2f} grams of honey left.')