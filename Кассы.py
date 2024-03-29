n = int(input())
checkouts, eventsline, overnightcnt = [tuple(map(int, input().split())) for _ in range(n)], [], 0
for i in range(n):
    checkout = checkouts[i]
    timeopen = checkout[0] * 60 + checkout[1]
    timeclose = checkout[2] * 60 + checkout[3]
    if timeopen == timeclose:
        overnightcnt += 1
    elif timeopen > timeclose:  # split into 2 events
        eventsline.append((timeopen, -1, i))
        eventsline.append((1440, 1, i))
        eventsline.append((0, -1, i))
        eventsline.append((timeclose, 1, i))
    else:
        eventsline.append((timeopen, -1, i))
        eventsline.append((timeclose, 1, i))
eventsline.sort()

openedcnt, allwork_timestart, allwork_timeend, allwork_timetotal = overnightcnt, 0, 0, 0
for event in eventsline:
    if event[1] == -1:
        openedcnt += 1
        if openedcnt == n:
            allwork_timestart = event[0]
    if event[1] == 1:
        if openedcnt == n:
            allwork_timetotal += event[0] - allwork_timestart
            allwork_timeend = event[0]
        openedcnt -= 1

if overnightcnt == n:
    print(1440)
else:
    print(allwork_timetotal)
