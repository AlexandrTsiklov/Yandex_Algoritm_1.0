n, k = map(int, input().split())
trees = list(map(int, input().split()))
L, R = 0, 0
length = 10**10
rm, rmx = 0, 0
l = 0
d = {}

while R < n:
    if l == k:
        m = L
        mx = R - 1
        if mx - m < length:
            length = mx - m
            rm = m
            rmx = mx
        if d[trees[L]] == 1:
            del d[trees[L]]
            l -= 1
        else:
            d[trees[L]] -= 1
        L += 1
    else:
        if R != n:
            if trees[R] not in d:
                d[trees[R]] = 0
                l += 1
            d[trees[R]] += 1
        R += 1

print(rm + 1, rmx + 1) #















