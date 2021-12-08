g, s_l = map(int, input().split())
w, s, dict_example, dict_our, total, summa = input(), input(), {}, {}, 0, 0

for char in w:
    if char not in dict_example:
        dict_example[char] = 0
    dict_example[char] += 1
    dict_our[char] = 0
we_were_there, ness_summa = None, len(dict_example)

for i in range(0, g):
    char_r = s[i]
    if char_r in dict_our:
        dict_our[char_r] += 1
        if dict_our[char_r] == dict_example[char_r]:
            summa += 1
        elif dict_our[char_r] > dict_example[char_r]:
            summa -= 1
if summa == ness_summa:
    total += 1

for i in range(g, s_l):
    char_r = s[i]
    char_l = s[i - g]

    if char_l in dict_our:
        dict_our[char_l] -= 1
        if dict_our[char_l] == dict_example[char_l]:
            summa += 1
        elif dict_our[char_l] == dict_example[char_l] - 1:
            summa -= 1

    if char_r in dict_our:
        dict_our[char_r] += 1
        if dict_our[char_r] == dict_example[char_r]:
            summa += 1
            we_were_there = True
        elif dict_our[char_r] > dict_example[char_r] and we_were_there:
            summa -= 1
            we_were_there = False

    if summa == ness_summa:
        total += 1

print(total)















