n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]


def check_list(l, m, k):
    count_otrezkov = 0
    for i in l:
        if m == 0:
            continue
        count_otrezkov += i // m
    return count_otrezkov >= k


def bin_search(lst, k):
    L, R = 0, max(lst) + 1
    while R != L:
        m = (R + L + 1) // 2
        if check_list(lst, m, k):
            L = m
        else:
            R = m - 1

    return L


print(bin_search(lst, k))