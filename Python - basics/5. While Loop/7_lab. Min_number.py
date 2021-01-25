import sys
input_num = input()
min_num = sys.maxsize

while input_num != 'Stop':
    input_num = int(input_num)
    if input_num < min_num:
        min_num = input_num
    input_num = input()

print(min_num)