class_count = int(input())
class_requirements = list(map(int, input().split()))
models_count = int(input())
models_dict, new_models_dict = {}, {}
for i in range(models_count):
    power, price = map(int, input().split())
    if power not in models_dict or models_dict[power] > price:
        models_dict[power] = price

models_dict = dict(sorted(models_dict.items(), reverse=True))
min_price = ''
for power in models_dict:
    if min_price == '':
        min_price = models_dict[power]
        new_models_dict[power] = models_dict[power]

    if models_dict[power] < min_price:
        min_price = models_dict[power]
        new_models_dict[power] = min_price

total_price = 0
new_models_dict = dict(sorted(new_models_dict.items()))
for req in class_requirements:
    ''' Чудом не ловит TL с циклом ниже, в идеале делать вместо него 2 указатель,
    чтобы каждый раз не бегать по меньшим мощностям'''
    for power in new_models_dict:
        if power >= req:
            total_price += new_models_dict[power]
            break

print(total_price)