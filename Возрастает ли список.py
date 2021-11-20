lst = list(map(int, input().split()))
flag = 'YES'
for i in range(1, len(lst)):
    if lst[i] <= lst[i - 1]:
        flag = 'NO'
        break
print(flag)