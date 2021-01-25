bee_population = int(input())
years = int(input())

for i in range(1, years + 1):
    bee_population = bee_population + (bee_population // 10) * 2
    if i % 5 == 0:
        bee_population = bee_population - (bee_population // 50) * 5
    bee_population = bee_population - (bee_population // 20) * 2

print(f'Beehive population: {bee_population}')