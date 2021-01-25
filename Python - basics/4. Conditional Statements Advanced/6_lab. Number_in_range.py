number = float(input())
if number in range(-100,101) and number != 0:
    print('Yes')
else:
    print('No')

# Variant 2
if -100 <= number <= 100 and number != 0:
    print('Yes')
else:
    print('No')