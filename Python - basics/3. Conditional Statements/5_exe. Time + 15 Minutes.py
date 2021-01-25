hour = int(input())
minute = int(input())
if minute >= 45:
    minute = (minute + 15) - 60
    hour = hour + 1
else:
    minute = 15 + minute
if hour == 24:
    hour = 0
if minute < 10:
    print(f'{hour}:0{minute}')
else:
    print(f'{hour}:{minute}')