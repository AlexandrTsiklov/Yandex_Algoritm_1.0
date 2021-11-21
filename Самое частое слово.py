with open('input.txt', 'r') as f:
    lst_words = f.read().split()
words_dict = {}

max_count = 0
for i in lst_words:
    if i not in words_dict:
        words_dict[i] = 1
    else:
        words_dict[i] += 1
    if words_dict[i] >= max_count:
        max_count = words_dict[i]

lst_max_words = [i for i in words_dict if words_dict[i] == max_count]
min_word = 'z' * 10**2
for i in lst_max_words:
    if i < min_word:
        min_word = i
print(min_word)  #