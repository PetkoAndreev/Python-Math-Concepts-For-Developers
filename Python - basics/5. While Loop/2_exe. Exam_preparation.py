num_bad_grades = int(input())
task_name = input()
task_grade = int(input())
task_counter = 0
task_sum_grades = 0
task_bad_grade_count = 0

while task_name != 'Enough':
    if task_grade <= 4:
        task_bad_grade_count += 1
    if task_bad_grade_count == num_bad_grades:
        print(f'You need a break, {num_bad_grades} poor grades.')
        break
    task_counter += 1
    task_sum_grades += task_grade
    prev_task = task_name
    task_name = input()
    if task_name == 'Enough':
        print(f'Average score: {(task_sum_grades / task_counter):.2f}')
        print(f'Number of problems: {task_counter}')
        print(f'Last problem: {prev_task}')
    else:
        task_grade = int(input())
