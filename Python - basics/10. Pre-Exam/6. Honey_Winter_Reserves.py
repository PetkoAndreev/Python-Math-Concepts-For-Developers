honey = float(input())
bee_name = input()
total_honey = 0

while bee_name != 'Winter has come':
    honey_collect = 0
    for i in range(1, 7):
        curr_month_honey = float(input())
        honey_collect += curr_month_honey
    if honey_collect < 0:
        print(f'{bee_name} was banished for gluttony')
    total_honey += honey_collect
    if total_honey >= honey:
        print(f'Well done! Honey surplus {(total_honey - honey):.2f}.')
        flag = True
        break
    bee_name = input()

if bee_name == 'Winter has come' and total_honey < honey:
    print(f'Hard Winter! Honey needed {(honey - total_honey):.2f}.')
elif bee_name == 'Winter has come':
    print(f'Well done! Honey surplus {(total_honey - honey):.2f}.')