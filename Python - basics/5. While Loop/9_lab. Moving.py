width = int(input())
length = int(input())
heigth = int(input())
apartment_space = width * length * heigth
box_space = 0

while True:
    box_num = input()
    if box_num == 'Done':
        print(f'{apartment_space - box_space} Cubic meters left.')
        break
    box_num = int(box_num)
    box_space += box_num
    if box_space >= apartment_space:
        print(f'No more free space! You need {box_space - apartment_space} Cubic meters more.')
        break