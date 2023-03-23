customers, eventsline = [tuple(map(int, input().split())) for _ in range(int(input()))], []
for i in range(len(customers)):
    if customers[i][1] - customers[i][0] >= 5:
        eventsline.append((customers[i][0], -1, i))
        eventsline.append((customers[i][1] - 5, 1, i))
eventsline.sort()

if len(eventsline) == 0:
    print(0, 10, 20)
elif len(eventsline) == 2:
    print(1, eventsline[0][0], eventsline[0][0] + 5)
else:
    cntlisten1, listeners1, ad1time, ad2time, maxcnt = 0, set(), 10, 20, -1
    for i in range(len(eventsline) - 1):
        event1 = eventsline[i]
        if event1[1] == -1:
            listeners1.add(event1[2])
            cntlisten1 += 1
        if cntlisten1 > maxcnt:
            maxcnt = cntlisten1
            ad1time = event1[0]
            ad2time = ad1time + 5
        cntlisten2 = 0
        for j in range(i + 1, len(eventsline)):
            event2 = eventsline[j]
            if event2[1] == -1:
                cntlisten2 += 1
            if (event2[0] - event1[0] >= 5) and (cntlisten1 + cntlisten2 > maxcnt):
                maxcnt, ad1time, ad2time = cntlisten1 + cntlisten2, event1[0], event2[0]
            if (event2[1] == 1) and (event2[2] not in listeners1):
                cntlisten2 -= 1
        if event1[1] == 1:
            cntlisten1 -= 1
            listeners1.remove(event1[2])

    print(maxcnt, ad1time, ad2time)
