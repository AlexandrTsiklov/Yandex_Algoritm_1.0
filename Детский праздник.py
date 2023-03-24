m, n = map(int, input().split())
workers = []
for i in range(n):
    blowuptime, balloonamt, resttime = map(int, input().split())
    workers.append([blowuptime, balloonamt, resttime, i, 0, 0, 0])  # 0, 0, 0 - сколько времени дул, сколько надул без перерыва, сколько надул всего
workers.sort()

while m > 0:
    mintotaltime, bestworkerid = 2 * 10**6, -1
    for i in range(len(workers)):  # перебираем всех помощников
        worker = workers[i]
        newtotaltime = worker[4] + worker[0]  # считаем суммарное время с учётом текущего шарика
        if newtotaltime <= mintotaltime:  # находим помощника, у которого оно минимально
            mintotaltime = newtotaltime
            bestworkerid = i
    workers[bestworkerid][4] = mintotaltime  # обновляем его суммарное время
    workers[bestworkerid][5] += 1  # обновляем сколько он надул без перерыва
    workers[bestworkerid][6] += 1  # обновляем сколько он надул всего

    if workers[bestworkerid][1] == workers[bestworkerid][5]:  # если пора сделать перерыв
        workers[bestworkerid][4] += workers[bestworkerid][2]  # увеличиваем суммарное время на время перерыва
        workers[bestworkerid][5] = 0  # и обнуляем надутые на одном дыхании шарики
    m -= 1  # уменьшаем количество шириков, которые осталось надуть

maxtime = -1
for worker in workers:
    if worker[5] == 0:  # если 0 надутых (т.е. он уже сделал перерыв)
        if worker[4] != 0:  # если он вообще хоть что-то надувал
            worker[4] -= worker[2]  # вычитаем у него время перерыва
    if worker[4] > maxtime:  # ищем работника с максимальным временем, это и будет ответ
        maxtime = worker[4]

workers.sort(key=lambda x: x[3])
print(max(0, maxtime))  # если не зашли в предыдущий for, значит никто ничего не надувал вообще
for worker in workers:
    print(worker[6], end=' ')
