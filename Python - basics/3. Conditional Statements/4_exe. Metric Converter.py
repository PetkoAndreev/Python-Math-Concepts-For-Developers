number = float(input())
type_to_convert = input()
result_type = input()

if type_to_convert == 'mm':
    if result_type == 'cm':
        converted_number = number/10
    elif result_type == 'm':
        converted_number = number/1000
elif type_to_convert == 'cm':
    if result_type == 'mm':
        converted_number = number*10
    elif result_type == 'm':
        converted_number = number/100
else:
    if result_type == 'mm':
        converted_number = number*1000
    elif result_type == 'cm':
        converted_number = number*100
print(f'{converted_number: .3f}')