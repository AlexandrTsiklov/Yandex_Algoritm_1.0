n, k = map(int, input().split())
numbers = list(map(int, input().split()))

R, summa, count = 0, numbers[0], 0
for L in range(n):
    while R < n:
        if summa == k:
            count += 1
            summa -= numbers[L]
            break
        elif summa < k:
            R += 1
            if R < n:
                summa += numbers[R]
        else:
            summa -= numbers[L]
            break

    if R == len(numbers) - 1:
        break

print(count)