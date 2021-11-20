operations_list = []
with open('input.txt', 'r') as f:
    for i in f.readlines():
        operations_list.append(i.split())

common_dict = {}


def deposit(surname, value):
    global common_dict
    if surname not in common_dict:
        common_dict[surname] = 0
    common_dict[surname] += value


def income(percent):
    global common_dict
    percent /= 100
    for key in common_dict:
        if common_dict[key] > 0:
            common_dict[key] += int(common_dict[key] * percent)


def balance(surname):
    global common_dict
    if surname not in common_dict:
        print('ERROR')
    else:
        print(common_dict[surname])


def withdraw(surname, value):
    global common_dict
    if surname not in common_dict:
        common_dict[surname] = 0
    common_dict[surname] -= value


def transfer(from_surname, to_surname, value):
    deposit(to_surname, value)
    withdraw(from_surname, value)


for i in operations_list:
    if i[0] == 'DEPOSIT':
        deposit(i[1], int(i[2]))
    elif i[0] == 'INCOME':
        income(int(i[1]))
    elif i[0] == 'BALANCE':
        balance(i[1])
    elif i[0] == 'WITHDRAW':
        withdraw(i[1], int(i[2]))
    else:
        transfer(i[1], i[2], int(i[3]))
