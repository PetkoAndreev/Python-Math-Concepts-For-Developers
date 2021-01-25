first_num = int(input())
second_num = int(input())
third_num = int(input())

for i in range (1, first_num + 1):
    for j in range (1, second_num + 1):
        for k in range (1, third_num + 1):
            if i % 2 == 0 and j > 1 and k % 2 == 0:
                for prime in range(2, j):
                    if (j % prime) == 0:
                        break
                else:
                    print(f'{i} {j} {k}')
