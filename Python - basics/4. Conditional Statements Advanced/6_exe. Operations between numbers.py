number1 = int(input())
number2 = int(input())
sign = input()

if sign == '+':
    result = number1 + number2

elif sign == '-':
    result = number1 - number2

elif sign == '*':
    result = number1 * number2

elif sign == '/' and number2 != 0:
    result = number1 / number2

elif sign == '%' and number2 != 0:
    result = number1 % number2

else:
    result = 0
    print(f'Cannot divide {number1} by zero')

if result % 2 == 0:
    text = 'even'
elif result % 2 == 1:
    text = 'odd'

if sign == '/' and number2 != 0:
    print(f'{number1} {sign} {number2} = {result:.2f}')

elif sign in('+', '-', '*'):
    print(f'{number1} {sign} {number2} = {result} - {text}')

elif sign == '%' and number2 != 0:
    print(f'{number1} {sign} {number2} = {result}')