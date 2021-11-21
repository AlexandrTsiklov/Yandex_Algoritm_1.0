import re
kw_count, true_register, true_digit = input().split()
key_word_list = []
if kw_count != '0':
    key_word_list = [input() for i in range(int(kw_count))]

s = ''
with open('input.txt', 'r') as f:
    for i in f.readlines():
        s += i.strip() + ' '

if true_digit == 'yes':
    that_list_we_get = re.findall(r'[a-zA-Z0-9_]*[a-zA-Z_]+[a-zA-Z0-9_]*', s)
else:
    that_list_we_get = re.findall(r'[a-zA-Z_]*[a-zA-Z_]+[a-zA-Z0-9_]*', s)

dict_params = {}
if true_register == 'yes':
    for i in that_list_we_get:
        if i not in dict_params:
            dict_params[i] = 0
        dict_params[i] += 1
else:
    for i in that_list_we_get:
        if i.lower() not in dict_params:
            dict_params[i.lower()] = 0
        dict_params[i.lower()] += 1

max_count = 0
if true_register == 'no':
    for i in range(len(key_word_list)):
        key_word_list[i] = key_word_list[i].lower()
for i in dict_params:
    if (dict_params[i] > max_count) and (i not in key_word_list):
        max_count = dict_params[i]
        max_value = i
print(max_value) #