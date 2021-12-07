from math import factorial
n = int(input())
treugs = [tuple(input().split()) for _ in range(n)]
treugs_count = 0

for point in treugs:
    dict_distanses = {}
    exceptions = set()
    for free_point in treugs:

        if free_point in exceptions:
            treugs_count -= 1
        exceptions.add(('-' + free_point[0], '-' + free_point[1]))

        distanse = (int(free_point[1]) - int(point[1]))**2 + (int(free_point[0]) - int(point[0]))**2
        if distanse not in dict_distanses:
            dict_distanses[distanse] = 0
        dict_distanses[distanse] += 1 #

    for dist in dict_distanses:
        es_count = dict_distanses[dist]
        if es_count > 1:
            treugs_count += int(factorial(es_count)/(factorial(es_count - 2) * 2))

print(treugs_count)
