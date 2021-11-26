import math

n, k = input().split()
arr1 = sorted(list(map(int, input().split())))
arr2 = list(map(int, input().split()))
print(arr1)
print(arr2)


def bin_search(arr, elem):
    length = len(arr)
    R, L = length, 0
    while R != L:
        m = (R + L) // 2
        if elem > arr[m]:
            L = m + 1
        else:
            R = m

    if R == length:
        return arr[R - 1] == elem
    return arr[R] == elem


for elem in arr2:
    if bin_search(arr1, elem):
        print('YES')
    else:
        print('NO')



