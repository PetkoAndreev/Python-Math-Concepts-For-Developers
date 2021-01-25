students = int(input())
tasks = int(input())
trainer_energy = int(input())
completed_tasks = 0
questions = 0

while trainer_energy > 0:
    trainer_energy = trainer_energy - (tasks * 2)
    students -= tasks
    trainer_energy = trainer_energy - (students * 2 * 3)
    questions = questions + (students * 2)
    completed_tasks += tasks
    if students < 10:
        print(f'The students are too few!')
        print(f'Problems solved: {completed_tasks}')
        break
    else:
        students = students + (students // 10)

if students >= 10:
    print(f'The trainer is too tired!')
    print(f'Questions asked: {questions}')