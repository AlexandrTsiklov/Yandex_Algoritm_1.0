t, d, n = map(int, input().split())
lst_coordinates = [list(map(int, input().split())) for i in range(n)]
min_dist = min(t, d)


# Ищем всех соседей вокруг
def get_points_around(current_point, distance):
    temporary_list = []
    for i in range(-distance, distance + 1):
        for j in range(-distance, distance + 1):
            if abs(i) + abs(j) <= distance and abs(i) + abs(j) != 0:
                temporary_list.append([current_point[0] + i, current_point[1] + j])
    temporary_list.append(current_point)
    return temporary_list


# Ищем общие точки между точками и возвращаем общие для последней
def lets_get_all_the_path(current_lst, whole_list, number, length, time):
    temp_points = []
    for i in current_lst:
        for j in whole_list[number]:
            summa = abs(i[0] - j[0]) + abs(i[1] - j[1])
            if summa <= time:
                if [j[0], j[1]] not in temp_points:
                    temp_points.append([j[0], j[1]])

    if number == length - 1:
        return temp_points
    else:
        return lets_get_all_the_path(temp_points, whole_list, number + 1, length, time)


from_start_to_end = [get_points_around(point, min_dist) for point in lst_coordinates]
if n == 1:
    result = get_points_around(lst_coordinates[0], min_dist)
else:
    result = lets_get_all_the_path(from_start_to_end[0], from_start_to_end, 1, n, t)
print(len(result))
for i in result:
    print(*i)  #