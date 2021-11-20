g, s_l = map(int, input().split())
w = input()
s = input()

length = len(w)

letters_of_word = {}
for i in w:
    if i not in letters_of_word:
        letters_of_word[i] = 0
    letters_of_word[i] += 1

count = 0
temporary_dict = {}

for i in range(len(s) - length + 1):
    if i == 0:
        for j in range(length):
            if s[i + j] not in temporary_dict:
                temporary_dict[s[i + j]] = 0
            temporary_dict[s[i + j]] += 1
    else:
        if s[i + length - 1] not in temporary_dict:
            temporary_dict[s[i + length - 1]] = 0
        temporary_dict[s[i + length - 1]] += 1
        if temporary_dict[s[i - 1]] > 1:
            temporary_dict[s[i - 1]] -= 1
        else:
            del temporary_dict[s[i - 1]]

    if temporary_dict == letters_of_word:
        count += 1

print(count)

