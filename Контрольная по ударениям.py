n = int(input())
words_dict = {}

for i in range(n):
    word = input()
    lower_word = word.lower()
    if lower_word not in words_dict:
        words_dict[lower_word] = set()
    words_dict[lower_word].add(word)

count = 0
s = input().split()
for word in s:
    lower_word = word.lower()
    if lower_word in words_dict:
        if word not in words_dict[lower_word]:
            count += 1
    else:
        flag = True
        count_cap = 0
        for i in word:
            if i.lower() != i:
                count_cap += 1
            if count_cap > 1:
                flag = False
                break
        if flag is False or count_cap == 0:
            count += 1

print(count) #



