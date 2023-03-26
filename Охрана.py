k, tests = int(input()), []  # статус ОК на интерпретаторе Python 3.11.2, Python 3.9 (PyPy 7.3.11) выдавал ML
for _ in range(k):
    dataline = input().split()
    n, events = int(dataline[0]), []
    for i in range(1, 2 * n, 2):
        arrivaltime = int(dataline[i])
        leavingtime = int(dataline[i + 1])
        events.append((arrivaltime, leavingtime))
    events.sort()

    if n == 1:
        print("Accepted" if events[0][0] == 0 and events[0][1] == 10000 else "Wrong Answer")
    for i in range(1, n):
        prevguard = events[i - 1]
        currguard = events[i]
        if (i == 1 and prevguard[0] != 0) or (prevguard[0] == currguard[0]) or (prevguard[1] < currguard[0]) or (prevguard[1] >= currguard[1]) or (i == n - 1 and currguard[1] != 10000) or (i > 1 and events[i - 2][1] >= currguard[0]):
            print("Wrong Answer")
            break
        if i == n - 1:
            print("Accepted")
