n = int(input())
sin_dict1 = {}
sin_dict2 = {}

for i in range(n):
    word, sin_word = input().split()
    sin_dict1[word] = sin_word
    sin_dict2[sin_word] = word

entered_word = input()
if entered_word in sin_dict1:
    print(sin_dict1[entered_word])
else:
    print(sin_dict2[entered_word])  #