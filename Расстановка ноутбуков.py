a1, b1, a2, b2 = map(int, input().split())
lst_1, lst_2, common_side = [a1, b1], [a2, b2], ''

flag = False
for i in range(2):
    for j in range(2):
        if lst_1[i] == lst_2[j]:
            common_side = lst_2[j]
            lst_1.pop(i)
            lst_2.pop(j)
            print(common_side, (lst_1[0] + lst_2[0]))
            flag = True
            break
    if flag is True:
        break

max_there = max(max(lst_1), max(lst_2))
max_list, min_list = [], []

if max_there in lst_1:
    max_list = lst_1
    min_list = lst_2
else:
    max_list = lst_2
    min_list = lst_1

if flag is False:
    if min(max_list) > max(min_list):
        print(min(max_list), max(max_list) + min(min_list))
    else:
        print(max(max_list), min(max_list) + min(min_list))  #
