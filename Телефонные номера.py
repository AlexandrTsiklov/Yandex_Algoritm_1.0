number_store1 = input()
new_number_store1 = ''
number_store2 = input()
new_number_store2 = ''
number_store3 = input()
new_number_store3 = ''
number = input()
new_number = ''

for i in number:
    if i.isdigit():
        new_number += i
if new_number[0] == '7':
    new_number = new_number.replace('7', '8', 1)

if number_store1 == '': number_store1 = '0'
if number_store2 == '': number_store2 = '0'
if number_store3 == '': number_store3 = '0'

for i, j, k in zip(number_store1, number_store2, number_store3):
    if i.isdigit():
        new_number_store1 += i
    if j.isdigit():
        new_number_store2 += j
    if k.isdigit():
        new_number_store3 += k


for i in [new_number_store1, new_number_store2, new_number_store3]:
    local = i
    if local[0] == '7':
        local = local.replace('7', '8', 1)
    if (new_number in local) and len(new_number) == 11:
        print('YES')
    elif (new_number[0] + '495' + new_number[1:] in local) and len(new_number) == 8:
        print('YES')
    else:
        print('NO')
#


