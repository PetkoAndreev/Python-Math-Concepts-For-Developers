n = int(input())
l = int(input())
fifth_start = 0

for first_symbol in range(1, n):
    for second_symol in range(1, n):
        fifth_start = 0
        if second_symol >= first_symbol:
            fifth_start = second_symol + 1
        else:
            fifth_start = first_symbol + 1
        for third_symol in range(97, 97 + l):
            for fourth_symol in range(97, 97 + l):
                for fifth_symol in range(fifth_start, n + 1):
                    print(str(first_symbol) + str(second_symol) + chr(third_symol) + chr(fourth_symol) + str(fifth_symol), end = ' ')
