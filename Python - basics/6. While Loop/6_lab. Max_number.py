import sys
input_num = input()
max_num = -sys.maxsize

while input_num != 'Stop':
    input_num = int(input_num)
    if input_num > max_num:
        max_num = input_num
    input_num = input()

print(max_num)