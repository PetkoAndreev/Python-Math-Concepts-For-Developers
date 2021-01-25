n = int(input())
current = 1
flag = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
        if current > n:
            flag = True
            break
        print(str(current) + ' ', end = '')
        current += 1
    if flag:
        break
    print()
