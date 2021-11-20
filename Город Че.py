n, val = map(int, input().split())
arr = list(map(int, input().split()))

L = 0
R = 1
count = 0

while True:
    if arr[R] - arr[L] > val and R > L:
        count += len(arr) - R
        L += 1
    else:
        R += 1

    if R == len(arr):
        break

print(count)