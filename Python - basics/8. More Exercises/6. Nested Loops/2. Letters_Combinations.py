first_letter = input()
second_letter = input()
third_letter = input()
counter = 0

for i in range(ord(first_letter), ord(second_letter) + 1):
    for j in range(ord(first_letter), ord(second_letter) + 1):
        for k in range(ord(first_letter), ord(second_letter) + 1):
            if j == ord(third_letter) or i == ord(third_letter) or  k == ord(third_letter):
                pass
            else:
                counter += 1
                print(f'{chr(i)}{chr(j)}{chr(k)}', end = ' ')

print(counter)