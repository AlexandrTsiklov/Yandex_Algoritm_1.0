with open('input.txt', 'r') as f:
    lst_words = f.read().split()
words_dict = {}
for i in lst_words:
    if i not in words_dict:
        words_dict[i] = 0
    else:
        words_dict[i] += 1
    print(words_dict[i])