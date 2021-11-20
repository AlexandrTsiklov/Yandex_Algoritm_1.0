lst = list()

while True:
    value = int(input())
    if value == -2 * 10**9:
        break
    else:
        lst.append(value)


def CONSTANT(get_list):
    if len(set(get_list)) == 1:
        return 'CONSTANT'
    else:
        return False


def ASCENDING(get_list):
    flag = 'ASCENDING'
    for i in range(1, len(get_list)):
        if lst[i] <= lst[i - 1]:
            flag = False
            break
    return flag


def WEAKLY_ASCENDING(get_list):
    flag = 'WEAKLY_ASCENDING'
    for i in range(1, len(get_list)):
        if lst[i] < lst[i - 1]:
            flag = False
            break
    return flag


def DESCENDING (get_list):
    flag = 'DESCENDING'
    for i in range(1, len(get_list)):
        if lst[i] >= lst[i - 1]:
            flag = False
            break
    return flag


def WEAKLY_DESCENDING(get_list):
    flag = 'WEAKLY_DESCENDING'
    for i in range(1, len(get_list)):
        if lst[i] > lst[i - 1]:
            flag = False
            break
    return flag


final_flag = False
for i in [CONSTANT(lst), ASCENDING(lst), WEAKLY_ASCENDING(lst), DESCENDING(lst), WEAKLY_DESCENDING(lst)]:
    if i is not False:
        final_flag = True
        print(i)
        break
if final_flag is False:
    print('RANDOM')