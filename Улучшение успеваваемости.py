a = int(input())
b = int(input())
c = int(input())
otcenki = a * 2 + b * 3 + c * 4
count = a + b + c


def bin_search(otcenki, count):
    L, R = 0, 10 ** 20
    while R != L:
        m = (R + L) // 2
        if otcenki + 5 * m < 3.5 * count + m:
            L = m + 1
        else:
            R = m
    return R


print(bin_search(otcenki, count))