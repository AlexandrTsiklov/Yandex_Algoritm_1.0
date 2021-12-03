from heapq import merge
n, l = map(int, input().split())
lst_pos = [sorted(list(map(int, input().split()))) for _ in range(n)]
for i in lst_pos:
    print(i)


def bin_search(l, lst1, lst2):
    L, R = min(lst1[0], lst2[0]), max(lst1[-1], lst2[-1])
    merged = list(merge(lst1, lst2))
    while R != L:
        m = (R + L + 1) // 2
        if merged[l - 1] >= m:
            L = m
        else:
            R = m - 1
    return L


for i in range(len(lst_pos)):
    for j in range(i + 1, len(lst_pos)):
        print(bin_search(l, lst_pos[i], lst_pos[j]))