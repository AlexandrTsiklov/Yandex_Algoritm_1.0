n, k = input().split()
arr1 = sorted(list(set(map(int, input().split()))))
arr2 = list(map(int, input().split()))


def bin_search(arr, elem):
    length = len(arr)
    R, L = length, 0
    while L < R:
        m = (R + L) // 2
        if elem > arr[m]:
            L = m + 1
        else:
            R = m

    if R == length:
        return R - 1
    return R


for elem in arr2:
    ind = bin_search(arr1, elem)

    if ind > 0 and abs(arr1[ind - 1] - elem) <= abs(arr1[ind] - elem):
        print(arr1[ind - 1])
    else:
        print(arr1[ind])




