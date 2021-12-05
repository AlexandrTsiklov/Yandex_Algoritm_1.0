l1, arr2 = int(input()), list(map(int, input().split()))
l2, arr1 = int(input()), list(map(int, input().split()))


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


min_dif, el1, el2 = 10 ** 10, '', ''
for elem in arr2:
    ind = bin_search(arr1, elem)

    if ind > 0 and abs(arr1[ind - 1] - elem) <= abs(arr1[ind] - elem):
        diff = abs(arr1[ind - 1] - elem)
        el = arr1[ind - 1]
    else:
        diff = abs(arr1[ind] - elem)
        el = arr1[ind]

    if diff < min_dif:
        min_dif = diff
        el1 = elem
        el2 = el

print(el1, el2)






