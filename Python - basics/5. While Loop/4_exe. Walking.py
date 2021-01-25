target_steps = 10000
daily_steps = input()
current_steps = 0

while daily_steps != 'Going home':
    daily_steps = int(daily_steps)
    current_steps += daily_steps
    if current_steps >= 10000:
        print(f'Goal reached! Good job!\n{current_steps - target_steps} steps over the goal!')
        break
    daily_steps = input()
if daily_steps == 'Going home':
    daily_steps = int(input())
    current_steps += daily_steps
    if current_steps >= 10000:
        print(f'Goal reached! Good job!\n{current_steps - target_steps} steps over the goal!')
    else:
        print(f'{target_steps - current_steps} more steps to reach goal.')

