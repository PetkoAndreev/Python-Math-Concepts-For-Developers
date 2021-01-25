num = int(input())
counter = 1

while True:
    if counter > num:
        break

    print(counter)
    counter = 2 * counter + 1