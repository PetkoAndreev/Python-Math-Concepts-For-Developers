person_name = input()
current_class = 0
counter_excluded = 0
sum_grades = 0
count_grades = 0

while current_class < 12:
    grade = float(input())
    sum_grades += grade

    if grade < 4.0:
        counter_excluded += 1

    if counter_excluded > 1:
        print(f'{person_name} has been excluded at {current_class} grade')
        break

    current_class += 1
    count_grades += 1

if counter_excluded < 2:
    print(f'{person_name} graduated. Average grade: {(sum_grades / count_grades):.2f}')