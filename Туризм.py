points_list = [tuple(map(int, input().split())) for _ in range(int(input()))]
roads_list = [tuple(map(int, input().split())) for _ in range(int(input()))]


def tyda_syda(point_list, start, finish, step, i_plus, what_add):
    high, my_dict = 0, {1: 0}
    for i in range(start, finish, step):
        if point_list[i][1] >= point_list[i + i_plus][1]:
            high += point_list[i][1] - point_list[i + i_plus][1]
            if point_list[i][0] != point_list[i + i_plus][0]:
                my_dict[what_add] = high
        else:
            my_dict[what_add] = high
    return my_dict

    high1, points_dict_ahead = 0, {1: 0}
    for i in range(1, len(points_list)):
        if points_list[i][1] >= points_list[i - 1][1]:
            high1 += points_list[i][1] - points_list[i - 1][1]
            if points_list[i][0] != points_list[i - 1][0]:
                points_dict_ahead[i + 1] = high1
        else:
            points_dict_ahead[i + 1] = high1




high2, points_dict_back = 0, {1: 0}
for i in range(-2, -len(points_list) - 1, -1):
    if points_list[i][1] >= points_list[i + 1][1]:
        high2 += points_list[i][1] - points_list[i + 1][1]
        if points_list[i][0] != points_list[i + 1][0]:
            points_dict_back[abs(i)] = high2
    else:
        points_dict_back[abs(i)] = high2

for road in roads_list:
    if road[0] < road[1]:
        print(points_dict_ahead[road[1]] - points_dict_ahead[road[0]])
    elif road[0] > road[1]:
        print(points_dict_back[road[0]] - points_dict_back[road[1]])
    else:
        print(0)