n, k = map(int, input().split())
s = input()
d, d1 = {}, {}
st = set(s)
total_sum = len(st)
for i in st:
    d[i] = 0
    d1[i] = False
L, R, length = 0, 1, 0
first_letter = 1

total = 0
mx_sum = -1
if n == 1:
    print(1, 1)
else:
    d[s[L]] += 1
    while True:

        if d[s[L]] <= k:
            if d1[s[L]] is False:
                total += 1
                d1[s[L]] = True
        elif total != 0:
            total -= 1

        go_fly = False
        while True:
            d[s[R]] += 1
            if d[s[R]] == k + 1 and s[R] == s[L]:
                d[s[R]] -= 1
                go_fly = True
                R += 1
                break
            if d[s[R]] == k + 1:
                total = 1
                for i in d:
                    d[i] = 0
                    d1[i] = False
                L = R
                R += 1
                d[s[L]] = 1
                d1[s[L]] = True
                if R == n:
                    break

            if d[s[R]] <= k:
                if d1[s[R]] is False:
                    total += 1
                    d1[s[R]] = True
            elif total != 0:
                total -= 1

            if total == total_sum:
                if R - L + 1 > mx_sum:
                    mx_sum = R + 1 - L
                    first_letter = min(R, L)
            R += 1
            if R == n:
                break

        if d[s[L]] > 0 and go_fly is False:
            d[s[L]] -= 1
        L += 1

        if R == n or L == n:
            break

        print(mx_sum, first_letter + 1)