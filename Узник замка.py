a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
max_list = [a, b, c]
max_list.remove(max(max_list))
if (max_list[0] <= d and max_list[1] <= e) or (max_list[0] <= e and max_list[1] <= d):
    print('YES')
else:
    print('NO')

