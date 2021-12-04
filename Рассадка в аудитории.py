n, d = map(int, input().split())
students_list_first = list(map(int, input().split()))
students_list = sorted(students_list_first)

L, R, max_var, dii = 0, 1, 1, {}
dii[students_list[0]] = 1

while R < len(students_list_first):
    if students_list[R] - students_list[L] > d:
        dii[students_list[R]] = dii[students_list[L]]
        L += 1
    else:
        max_var += 1
        dii[students_list[R]] = max_var
    R += 1

print(max_var)
for i in students_list_first:
    print(dii[i], end=' ')