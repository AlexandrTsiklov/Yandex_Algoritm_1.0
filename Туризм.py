n = int(input())
points_dict = {}
for i in range(1, n + 1):
    points_dict[i] = list(map(int, input().split()))
roads_list = [list(map(int, input().split())) for i in range(int(input()))]

for road in roads_list:
    point_start = road[0]
    point_finish = road[1]

    height = 0
    if point_start > point_finish:
        for point in range(point_start, point_finish, -1):
            if points_dict[point - 1][1] > points_dict[point][1]:
                height += points_dict[point - 1][1] - points_dict[point][1]

    else:
        for point in range(point_start, point_finish):
            if points_dict[point + 1][1] > points_dict[point][1]:
                height += points_dict[point + 1][1] - points_dict[point][1]

    print(height)  #
