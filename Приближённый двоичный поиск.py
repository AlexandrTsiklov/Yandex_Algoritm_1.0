import math

n, k = input().split()
arr1 = list(map(int, input().split()))
set1 = set(arr1)
sorted_set = sorted(list(set1))
arr2 = list(map(int, input().split()))


def bin_search(arr, elem):
    length = len(arr)
    R, L = length, 0
    while R != L:
        m = (R + L + 1) // 2
        if elem > arr[m]:
            L = m
        else:
            R = m - 1

    if R == length:
        return R - 1
    return R


for elem in arr2:
    print(bin_search(arr1, elem))




