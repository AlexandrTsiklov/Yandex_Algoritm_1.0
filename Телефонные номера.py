number = input()
number_1 = input()
number_2 = input()
number_3 = input()

number_f = [i for i in number if i.isdigit()]
number_1f = [i for i in number_1 if i.isdigit()]
number_2f = [i for i in number_2 if i.isdigit()]
number_3f = [i for i in number_3 if i.isdigit()]
numbers = [number_f, number_1f, number_2f, number_3f]

for i in range(len(numbers)):
    if numbers[i][0] != '7' and numbers[i][0] != '8' and len(numbers[i]) < 11:
        numbers[i] = ['8'] + numbers[i]
    elif len(numbers[i]) == 11:
        numbers[i][0] = '8'
    if len(numbers[i]) == 8:
        numbers[i] = numbers[i][:1] + ['4', '9', '5'] + numbers[i][1:]

for number in numbers[1:]:
    if number == numbers[0]:
        print('YES')
    else:
        print('NO')


