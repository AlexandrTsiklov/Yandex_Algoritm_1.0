data = list(map(int, input().split()))
coordinates = {}

# Подготовка данных
for i in range(data[2]):
    coordinates[i] = list(map(int, input().split()))
field = [[] for i in range(data[0])]


# Количество бомб вокруг
def bombs_count(stroka, stolbets):
    count = 0
    for i in range(stroka - 1, stroka + 2):
        for j in range(stolbets - 1, stolbets + 2):
            try:
                if field[i][j] == '*' and i >= 0 and j >= 0:
                    count += 1
            except IndexError:
                continue
    return count


# Строим поле
for i in range(len(field)):
    for j in range(data[1]):
        flag = False
        for point in coordinates:
            if i + 1 == coordinates[point][0] and j + 1 == coordinates[point][1]:
                flag = True
        if flag:
            field[i].append('*')
        else:
            field[i].append(0)


# Заполняем поле
for i in range(len(field)):
    for j in range(data[1]):
        if field[i][j] != '*':
            field[i][j] = bombs_count(i, j)

for i in field:
    print(*i)


