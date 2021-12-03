students, teachers = map(int, input().split())
teachers_list = [tuple(map(int, input().split())) for _ in range(teachers)]
teachers_list.sort()

total = 0
start = 1
end = -1

for i in teachers_list:
    if i[0] <= end:
        if i[1] > end:
            total += i[1] - end
            end = i[1]
    else:
        start = i[0]
        end = i[1]
        total += end - start + 1

print(students - total)





