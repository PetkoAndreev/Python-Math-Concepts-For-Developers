import math
students = int(input())
tasks = int(input())

total_tasks = students * math.ceil(tasks * 2.8) + (students * (tasks//3))
total_memory = 5 * math.ceil(total_tasks / 10)

print(f'{total_memory} KB needed')
print(f'{total_tasks} submissions')