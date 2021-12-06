n, k = map(int, input().split())
numbers = list(map(int, input().split()))

L, R, summa, count = 0, 0, numbers[0], 0

while L < n - 1:
    if summa <= k:
        if summa == k:
            count += 1

        if R == n - 1:
            summa -= numbers[L]
            L += 1
        else:
            R += 1
            summa += numbers[R]
    else:
        summa -= numbers[L]
        L += 1

print(max(int(numbers[0] == k), count))