n, k = map(int, input().split())#
lst = list(map(int, input().split()))
dct = {}
lst_values = []

for i in lst:
    if i not in dct:
        dct[i] = 0
        lst_values.append(i)
    dct[i] += 1
lst_values = sorted(lst_values)
length = len(lst_values)

L, R = 0, 1
count = 0

if length == 1:
    count = 1
elif length == 2:
    if lst_values[1] / lst_values[0] <= k:
        if dct[lst_values[0]] > 1:
            count += 3
        if dct[lst_values[0]] > 2:
            count += 1
        if dct[lst_values[1]] > 1:
            count += 3
        if dct[lst_values[1]] > 2:
            count += 1
else:
    while L < length:
        while R < length:
            if lst_values[R] / lst_values[L] <= k:
                if R - L - 1 >= 1:
                    multi = R - L - 1
                    count += multi * 6
                if dct[lst_values[R]] > 1:
                    count += 3
                if dct[lst_values[L]] > 1:
                    count += 3
                R += 1
            else:
                break
        if dct[lst_values[L]] > 2:
            count += 1
        L += 1
        R = L + 1

print(count) #
















