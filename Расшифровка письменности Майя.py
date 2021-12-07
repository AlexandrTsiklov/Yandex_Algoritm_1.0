g, s_l = map(int, input().split())
w, s, true_dict1, true_dict2, total = input(), input(), {}, {}, 0

for letter in s:
    true_dict1[letter] = 0
    true_dict2[letter] = 0
for letter in w:
    if letter not in true_dict1:
        true_dict1[letter] = 0
    true_dict1[letter] += 1

calc_length = 0
for key in true_dict1:
    if true_dict1[key] > 0:
        calc_length += 1

summa = 0
for char in s[0:g - 1]:
    true_dict2[char] += 1
for letter in w:
    if true_dict2[letter] == true_dict1[letter] and true_dict1[letter] > 0:
        summa += 1

L, R = 0, g
while R < s_l:
    if (true_dict1[s[L]] > 0) and (true_dict2[s[L]] == true_dict1[s[L]]):
        summa -= 1
    elif (true_dict1[s[L]] > 0) and (true_dict2[s[L]] - 1 == true_dict1[s[L]]):
        summa += 1

    if (true_dict1[s[R]] > 0) and (true_dict2[s[R]] == true_dict1[s[R]]):
        summa += 1

    true_dict2[s[L]] -= 1
    true_dict2[s[R]] += 1

    if summa == calc_length:
        total += 1
    L += 1
    R += 1

print(total)








