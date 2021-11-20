class_count = int(input())
class_requirements = list(map(int, input().split()))
models_count = int(input())
models_dict = {}
for i in range(models_count):
    power, price = map(int, input().split())
    if power not in models_dict or models_dict[power] > price:
        models_dict[power] = price

summa = 0
for i in class_requirements:
    m = 10**10
    price = 0
    for j in models_dict:
        if j >= i and models_dict[j] < m:
            m = models_dict[j]
            price = models_dict[j]
    summa += price

print(summa)