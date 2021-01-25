import math
students = int(input())
seasons = int(input())

for i in range (1, seasons + 1):
    first_exam = math.ceil(students * 0.9)
    second_exam = math.ceil(first_exam * 0.9)
    continue_students = math.ceil(second_exam * 0.8)
    if i % 3 == 0:
        students = continue_students + math.ceil(continue_students * 0.15)
    else:
        students = continue_students + math.ceil(continue_students * 0.05)

print(f'Students: {students}')