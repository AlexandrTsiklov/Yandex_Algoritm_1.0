N, x, y = map(int, input().split())


def bin_search(N, x, y):
    L, R = 1, N * max(x, y)

    if N <= 2:
        return N * min(x, y)
    else:
        time_for_first_copy = min(x, y)
        while R != L:
            m = (R + L) // 2
            if m // x + m // y + 1 < N:
                L = m + 1
            else:
                R = m
        return R + time_for_first_copy


print(bin_search(N, x, y))