n, m = map(int, input().split())
segments, eventsline = [], []
for _ in range(n):
    segment = list(map(int, input().split()))
    segments.append((min(segment), max(segment)))
points = list(map(int, input().split()))
for segment in segments:
    eventsline.append((segment[0], 0))  # segment start
    eventsline.append((segment[1], 2))  # segment finish
for point in points:
    eventsline.append((point, 1))  # point position
eventsline.sort()

segmentscnt, point_segmentscnt = 0, {}
for event in eventsline:
    if event[1] == 1:
        point_segmentscnt[event[0]] = segmentscnt
    if event[1] == 0:
        segmentscnt += 1
    if event[1] == 2:
        segmentscnt -= 1

for point in points:
    print(point_segmentscnt[point], end=' ')
