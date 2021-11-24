k = int(input())  # > 1
s = input()  # > k

L = 0
R = k
length = len(s)
count = 0

while L < length - k + 1:
    flag = True
    r_local = R
    l_local = L

    while flag:
        if r_local == length:
            flag = False
            break

        if s[l_local] == s[r_local]:
            count += 1
            l_local += 1
            r_local += 1
        else:
            flag = False
            break

        if l_local - L == k:
            l_local = L

    L += 1
    R += 1

print(count)


