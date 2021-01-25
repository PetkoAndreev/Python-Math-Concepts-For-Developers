last_sector = input()
first_sector_rows = int(input())
odd_row_seats = int(input())
num_rows = first_sector_rows
counter = 0

for sector in range(65, ord(last_sector) + 1):
    for row in range(1, num_rows + 1):
        if row % 2 == 0:
            num_seats = odd_row_seats + 2
        else:
            num_seats = odd_row_seats
        for seat in range(1, num_seats + 1):
            counter += 1
            curr_seat = 96 + seat
            print(f'{chr(sector)}{row}{chr(curr_seat)}')
    num_rows += 1
print(counter)