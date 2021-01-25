first_couple = int(input())
second_couple = int(input())
first_couple_end = int(input())
second_couple_end = int(input())

for i in range (first_couple, (first_couple + first_couple_end + 1)):
    first_prime = 0
    for prime in range(2, i):
        if (i % prime) == 0:
            break
    else:
        first_prime = i
    for j in range(second_couple, (second_couple + second_couple_end + 1)):
        for prime in range(2, j):
            if (j % prime) == 0:
                break
        else:
            if first_prime != 0:
                print(f'{first_prime}{j}')
