points_list = [tuple(map(int, input().split())) for _ in range(int(input()))]
roads_list, length = [tuple(map(int, input().split())) for _ in range(int(input()))], len(points_list)


def total_height(point_list, first_elem, start, finish, step, i_plus, what_add):
    high, my_dict = 0, {first_elem: 0}
    for i in range(start, finish, step):
        if point_list[i][1] > point_list[i + i_plus][1]:
            high += point_list[i][1] - point_list[i + i_plus][1]
        my_dict[abs(i + what_add)] = high
    return my_dict


points_dict_ahead = total_height(points_list, 1, 1, length, 1, -1, 1)
points_dict_back = total_height(points_list, length, -2, -length - 1, -1, 1, length + 1)

for road in roads_list:
    if road[0] < road[1]:
        print(points_dict_ahead[road[1]] - points_dict_ahead[road[0]])
    else:
        print(points_dict_back[road[1]] - points_dict_back[road[0]])

