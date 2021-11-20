with open('input.txt', 'r') as f:
    lst_words = f.read().split()
customers_dict = {}


for i in range(0, len(lst_words) - 2, 3):
    if lst_words[i] not in customers_dict:
        customers_dict[lst_words[i]] = {}
    if lst_words[i + 1] not in customers_dict[lst_words[i]]:
        customers_dict[lst_words[i]][lst_words[i + 1]] = 0
    customers_dict[lst_words[i]][lst_words[i + 1]] += int(lst_words[i + 2])

for client in sorted(customers_dict):
    print(client + ':')
    for goods in sorted(customers_dict[client]):
        print(goods, customers_dict[client][goods])