jury_members = int(input())
presentation = input()
presentation_grades = float(input())
num_pres = 0
total_avg_grade = 0

while presentation != 'Finish':
    sum_grades = 0
    count_grades = 0

    while count_grades <= jury_members:
        count_grades += 1
        sum_grades += presentation_grades
        if count_grades == jury_members:
            break
        presentation_grades = float(input())
    pres_avg_grade = sum_grades / jury_members
    print (f'{presentation} - {pres_avg_grade:.2f}.')
    total_avg_grade += pres_avg_grade
    num_pres += 1
    presentation = input()
    if presentation == 'Finish':
        print(f'Student\'s final assessment is {(total_avg_grade/num_pres):.2f}.')
    else:
        presentation_grades = float(input())
