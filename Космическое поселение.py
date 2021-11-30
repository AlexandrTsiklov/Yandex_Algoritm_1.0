n, a, b, w, h = map(int, input().split())


def bin_search(n, a, b, w, h):
    L, R = 0, w
    while R > L:
        m = (R + L + 1) // 2
        w_one_build1 = a + 2 * m
        h_one_build1 = b + 2 * m

        w_one_build2 = b + 2 * m
        h_one_build2 = a + 2 * m

        val1 = (w // w_one_build1) * (h // h_one_build1)
        val2 = (w // w_one_build2) * (h // h_one_build2)
        if max(val1, val2) >= n:
            L = m
        else:
            R = m - 1
    return L


print(bin_search(n, a, b, w, h))