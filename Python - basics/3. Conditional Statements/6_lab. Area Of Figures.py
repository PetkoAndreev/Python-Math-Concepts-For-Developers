import math
figure = input()
if figure == 'square':
    side_one = float(input())
    print(f'{side_one*side_one: .3f}')
elif figure == 'rectangle':
    side_one = float(input())
    side_two = float(input())
    print(f'{side_one * side_two: .3f}')
elif figure == 'circle':
    radius = float(input())
    print(f'{math.pi * (radius*radius): .3f}')
else:
    side = float(input())
    height = float(input())
    print(f'{(side*height)/2: .3f}')