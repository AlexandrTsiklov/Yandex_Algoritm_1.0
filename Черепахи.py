n = int(input())
lst_tuple = []
for i in range(int(n)):
    lst_tuple.append(list(map(int, input().split())))
final_list = []

for i in lst_tuple:
    if i[0] + i[1] == n - 1:
        final_list.append(str(i[0]) + '*' + str(i[1]))

print(len(set(final_list)))
