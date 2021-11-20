school_boys_count = int(input())
common_languages, at_least_one_language = set(), []


for i in range(school_boys_count):
    personal_set, number = set(), int(input())

    for j in range(number):
        personal_set.add(input())

    if common_languages == set():
        common_languages = personal_set
    else:
        common_languages = common_languages.intersection(personal_set)
    at_least_one_language += list(personal_set)


set_at_least_one_language = set(at_least_one_language)
print(len(common_languages))
print(*list(common_languages), sep='\n')
print(len(set_at_least_one_language))
print(*list(set_at_least_one_language), sep='\n')




