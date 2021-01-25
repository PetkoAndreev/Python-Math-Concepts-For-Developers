vacation = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minion = int(input())
truck = int(input())

if puzzles + dolls + bears + minion + truck >= 50:
    prize = puzzles*2.60 + dolls*3 + bears*4.10 + minion*8.20 + truck*2
    discount_prize = prize - 0.25*prize
    total_prize = discount_prize - discount_prize*0.1
    if total_prize - vacation >= 0:
        print(f'Yes!{total_prize - vacation: .2f} lv left.')
    else:
        print(f'Not enough money!{abs(total_prize - vacation): .2f} lv needed.')
else:
    prize = puzzles * 2.60 + dolls * 3 + bears * 4.10 + minion * 8.20 + truck * 2
    total_prize = prize - prize * 0.1
    if total_prize - vacation >= 0:
        print(f'Yes!{total_prize - vacation: .2f} lv left.')
    else:
        print(f'Not enough money!{abs(total_prize - vacation): .2f} lv needed.')