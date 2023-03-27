def gettime(time):
    hours, minutes = time.split(':')
    return int(hours) * 60 + int(minutes)

n, m = map(int, input().split())
events, cities = [], dict((key, 0) for key in range(1, n + 1))
for i in range(1, n + 1):
    cities[i] = 0

overnight = 0
for _ in range(m):
    route = input().split()
    deptime, arrtime = gettime(route[1]), gettime(route[3])
    depcity, arrcity = int(route[0]), int(route[2])
    events.append((deptime, 1, depcity))
    cities[depcity] -= 1
    events.append((arrtime, -1, arrcity))
    cities[arrcity] += 1
    if arrtime < deptime:
        overnight += 1
events.sort()

badschedule = False
for event in events:
    if cities[event[2]] != 0:
        badschedule = True
        print(-1)
        break

if not badschedule:
    buscount = 0
    for event in events:
        city = event[2]
        if event[1] == -1:  # if arrival
            cities[city] += 1
        if event[1] == 1:  # if departure
            if cities[city] == 0:
                buscount += 1
            else:
                cities[city] -= 1
    print(buscount + overnight)
