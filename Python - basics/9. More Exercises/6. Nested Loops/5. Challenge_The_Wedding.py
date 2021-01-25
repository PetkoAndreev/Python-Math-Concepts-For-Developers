number_mans = int(input())
number_womens = int(input())
number_tables = int(input())
counter = 0

for i in range(1, number_mans + 1):
    for j in range(1, number_womens + 1):
        counter += 1
        if counter <= number_tables:
            print(f'({i} <-> {j})', end = ' ')