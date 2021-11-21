a, b, n, m = int(input()), int(input()), int(input()), int(input())
train1_set = set()
train2_set = set()


def how_much_time(interval, count, my_set):
    for i in range(interval + 1):
        for j in range(interval + 1):
            my_set.add(i + count + (count - 1) * interval + j)
    return my_set


times_1 = how_much_time(a, n, train1_set)
times_2 = how_much_time(b, m, train2_set)
result = times_1.intersection(times_2)

if result != set():
    print(min(result), max(result))
else:
    print(-1)  #



