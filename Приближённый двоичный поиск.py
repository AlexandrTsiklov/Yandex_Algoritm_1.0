n, k = input().split()
arr1 = list(map(int, input().split()))
set1 = set(arr1)
sorted_set = sorted(list(set1))
len_set = len(sorted_set)
arr2 = list(map(int, input().split()))


def bin_search(arr, elem):
    length = len(arr)
    R, L = length, 0
    while L < R:
        m = (R + L + 1) // 2

        if m == length:
            break

        if elem > arr[m]:
            L = m
        else:
            R = m - 1

    if R == length:
        return R - 1
    return R


for elem in arr2:
    ind = bin_search(sorted_set, elem)
    dif1 = abs(sorted_set[ind] - elem)
    try:
        dif2 = abs(sorted_set[ind + 1] - elem)
    except:
        dif2 = 10 ** 5

    if dif1 > dif2:
        print(sorted_set[ind + 1])
    else:
        print(sorted_set[ind])




