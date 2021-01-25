city = input()
sales_quantity = float(input())
if city == 'Sofia' and 0 <= sales_quantity <= 500:
    print(f'{0.05*sales_quantity:.2f}')
elif city == 'Sofia' and 500 < sales_quantity <= 1000:
    print(f'{0.07*sales_quantity:.2f}')
elif city == 'Sofia' and 1000 < sales_quantity <= 10000:
    print(f'{0.08*sales_quantity:.2f}')
elif city == 'Sofia' and sales_quantity > 10000:
    print(f'{0.12*sales_quantity:.2f}')
elif city == 'Varna' and 0 <= sales_quantity <= 500:
    print(f'{0.045*sales_quantity:.2f}')
elif city == 'Varna' and 500 < sales_quantity <= 1000:
    print(f'{0.075*sales_quantity:.2f}')
elif city == 'Varna' and 1000 < sales_quantity <= 10000:
    print(f'{0.1*sales_quantity:.2f}')
elif city == 'Varna' and sales_quantity > 10000:
    print(f'{0.13*sales_quantity:.2f}')
elif city == 'Plovdiv' and 0 <= sales_quantity <= 500:
    print(f'{0.055*sales_quantity:.2f}')
elif city == 'Plovdiv' and 500 < sales_quantity <= 1000:
    print(f'{0.08*sales_quantity:.2f}')
elif city == 'Plovdiv' and 1000 < sales_quantity <= 10000:
    print(f'{0.12*sales_quantity:.2f}')
elif city == 'Plovdiv' and sales_quantity > 10000:
    print(f'{0.145*sales_quantity:.2f}')
else:
    print('error')