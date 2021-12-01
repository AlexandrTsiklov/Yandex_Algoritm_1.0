n, count_br, count_p_in_br = map(int, input().split())
lst_rost = [int(input()) for _ in range(n)]
sorted_lst_rost = sorted(lst_rost)


def check_brigadu(rost_lst, count_brig, count_people, em):
    length = len(rost_lst)
    flag = False
    for ind_rost in range(length - count_people + 1):
        count = 0
        for rost in range(ind_rost, length - count_people + 1, count_people):
            if rost_lst[rost + count_people - 1] - rost_lst[rost] <= em:
                count += 1
            if count == count_brig:
                flag = True
                break
        if flag is True:
            break
    return flag


def bin_search(count_brig, count_pers_in_br, rost_lst):
    L, R = 0, sorted_lst_rost[-1] + 1
    while R != L:
        m = (R + L) // 2
        if not check_brigadu(rost_lst, count_brig, count_pers_in_br, m):
            L = m + 1
        else:
            R = m
    return R


print(bin_search(count_br, count_p_in_br, sorted_lst_rost))