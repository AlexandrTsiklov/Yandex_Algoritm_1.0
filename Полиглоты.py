boys_count, sets_languages = int(input()), []

for i in range(boys_count):
    personal_set = set()
    for j in range(int(input())):
        personal_set.add(input())
    sets_languages.append(personal_set)
sets_languages_c = sets_languages.copy()

if boys_count > 1:
    for i in range(1, len(sets_languages)):
        sets_languages[i] = sets_languages[i - 1].intersection(sets_languages[i])
        sets_languages_c[i] = sets_languages_c[i - 1].union(sets_languages_c[i])

print(len(sets_languages[-1]))
for i in sets_languages[-1]:
    print(i)
print(len(sets_languages_c[-1]))
for i in sorted(sets_languages_c[-1], reverse=True):
    print(i)