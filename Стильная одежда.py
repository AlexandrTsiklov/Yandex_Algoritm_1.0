l1, line1 = int(input()), list(map(int, input().split()))
l2, line2 = int(input()), list(map(int, input().split()))
difference = 10 ** 8


def merge_modified(arr1, arr2):
    ind1 = ind2 = 0
    merged_arr, final_len = [], len(arr1) + len(arr2)
    ind = 0
    pair_dict1 = {}
    pair_dict2 = {}
    t_ind1, t_ind2 = 0, 0
    flag = None

    for i in range(final_len):
        if ind1 != len(arr1) and (ind2 == len(arr2) or arr1[ind1] < arr2[ind2]):
            merged_arr.append(arr1[ind1])
            ind1 += 1
            if flag is None:
                flag = True
            if flag is False and ind != 0:
                flag = True
                if merged_arr[ind] in pair_dict1:
                    pair_dict2[merged_arr[ind]] = merged_arr[ind - 1]
                else:
                    pair_dict1[merged_arr[ind]] = merged_arr[ind - 1]
        else:
            merged_arr.append(arr2[ind2])
            ind2 += 1
            if flag is None:
                flag = False
            if flag is True and ind != 0:
                flag = False
                if merged_arr[ind] in pair_dict1:
                    pair_dict2[merged_arr[ind]] = merged_arr[ind - 1]
                else:
                    pair_dict1[merged_arr[ind]] = merged_arr[ind - 1]

        ind += 1
    return pair_dict1, pair_dict2


p_dict1, p_dict2 = merge_modified(line1, line2)
for i in p_dict1:
    if abs(i - p_dict1[i]) < difference:
        difference = abs(i - p_dict1[i])
        elem1 = i
        elem2 = p_dict1[i]
flag = False
for i in p_dict2:
    if abs(i - p_dict2[i]) < difference:
        flag = True
        difference = abs(i - p_dict2[i])
        elem3 = i
        elem4 = p_dict2[i]

if flag is True:
    print(elem3, elem4)
else:
    print(elem1, elem2)







