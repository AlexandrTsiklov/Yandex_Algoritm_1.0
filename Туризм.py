points_list = [tuple(map(int, input().split())) for _ in range(int(input()))]
roads_list = [tuple(map(int, input().split())) for _ in range(int(input()))]
points_dict_ahead = {1: 0}

high = 0
for i in range(1, len(points_list)):
    if points_list[i][1] >= points_list[i - 1][1]:
        high += points_list[i][1] - points_list[i - 1][1]
        if points_list[i][0] != points_list[i - 1][0]:
            points_dict_ahead[i + 1] = high
    else:
        points_dict_ahead[i + 1] = high

print(points_dict_ahead)






