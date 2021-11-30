n = int(input())
m = int(input())
t = int(input())


def bin_search(en, em, te):
    L, R = 0, max(en, em) // 2 + 1
    sum_plates = em * en

    while R != L:
        m = (R + L) // 2

        new_en = en - m * 2
        new_em = em - m * 2

        if sum_plates - (new_en * new_em) <= te:
            L = m + 1
        else:
            R = m

    return R - 1


print(bin_search(n, m, t))