import sys
n = int(input())
odd_sum = 0.00
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0.00
even_min = sys.maxsize
even_max = -sys.maxsize
'''
if n == 0:
    print(f'OddSum={odd_sum},')
    print(f'OddMin=No,')
    print(f'OddMax=No,')
    print(f'EvenSum={even_sum},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
else:
'''
for i in range(1, n + 1):
    num = float(input())
    if i % 2 == 0:
        even_sum += num
        if num < even_min:
            even_min = num
        if num > even_max:
            even_max = num
    else:
        odd_sum += num
        if num < odd_min:
            odd_min = num
        if num > odd_max:
            odd_max = num

print(f'OddSum={odd_sum:.2f},')
if odd_min != sys.maxsize:
    print(f'OddMin={odd_min:.2f},')
else:
    print('OddMin=No,')
if odd_max != -sys.maxsize:
    print(f'OddMax={odd_max:.2f},')
else:
    print('OddMax=No,')

print(f'EvenSum={even_sum:.2f},')
if even_min != sys.maxsize:
    print(f'EvenMin={even_min:.2f},')
else:
    print('EvenMin=No,')
if even_max != -sys.maxsize:
    print(f'EvenMax={even_max:.2f}')
else:
    print('EvenMax=No')