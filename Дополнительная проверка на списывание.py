import re
kw_count, true_register, true_digit = input().split()
key_word_list, max_value = [], 0
if kw_count != '0':
    key_word_list = [input() for i in range(int(kw_count))]


def check_un(s, register, digit):
    alpha = '_QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm1234567890'
    if register == 'no':
        s = s.lower()

    local_lst, local_length, local_s, i = [], len(s), '', 0

    while i < local_length:
        if s[i] in alpha and ((local_s == '' and (digit == 'yes' or s[i].isdigit() is False)) or local_s != ''):
            local_s += s[i]
            if i + 1 == local_length and local_s != '':
                local_lst.append(local_s)
        elif local_s != '':
            local_lst.append(local_s)
            local_s = ''
        i += 1
    return local_lst


with open('input.txt', 'r') as f:
    total = []
    for i in f.readlines():
        total += i.split()#

d = {}
for s in total:
    rez = check_un(s, true_register, true_digit)
    if rez:
        for i in rez:
            if i not in key_word_list:
                if i not in d:
                    d[i] = 0
                d[i] += 1

count = 0
for i in d:
    if d[i] > count:
        count = d[i]
        max_value = i
print(max_value)