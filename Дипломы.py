w, h, n = map(int, input().split())


def bin_search(w, h, n):
    L, R = 0, n * w

    while R != L:
        m = (R + L) // 2
        if (m // w) * (m // h) < n:
            L = m + 1
        else:
            R = m
    return R


print(bin_search(w, h, n))
            



