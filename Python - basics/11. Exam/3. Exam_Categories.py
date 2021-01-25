complexity = int(input())
rotation = int(input())
pages = int(input())

if complexity >= 80 and rotation >= 80 and pages >= 8:
    print('Legacy')
elif complexity >= 80 and rotation <= 10:
    print('Master')
elif complexity <= 30 and pages <= 1:
    print('Easy')
elif complexity <= 10:
    print('Elementary')
elif rotation >= 50 and pages >= 2:
    print('Hard')
else:
    print('Regular')

'''
Legacy	>= 80	>= 80	>= 8
Master	>= 80	<= 10	аny
Hard	any	>= 50	>= 2
Regular	any	any	any
Easy	<= 30	any	<= 1
Elementary	<= 10	any	any
Първо проверяваме Legacy, но не ни достига "завъртяност". 
Проверяваме Master, но "завъртяността" ни е в повече. 
Проверяваме Easy и Elementary, но сложността ни е по-голяма.
Проверяваме Hard, където изпълняваме и трите условия, съответно това е категорията на изпита.

'''