n, m = map(int, input().split())
otr_list = [tuple(map(int, input().split())) for _ in range(n)]
points = tuple(map(int, input().split()))

look_at_that, pdict = [], {}
for point in points:
    pdict[point] = 0

for otr in otr_list:
    look_at_that.append((min(otr), 0))
    look_at_that.append((max(otr), 2))
for point in points:
    look_at_that.append((point, 1))

look_at_that.sort()
i_include_this_count = 0

for i in range(len(look_at_that)):
    if look_at_that[i][1] == 0:
        i_include_this_count += 1
    elif look_at_that[i][1] == 2:
        i_include_this_count -= 1
    else:
        pdict[look_at_that[i][0]] = i_include_this_count

for point in points:
    print(pdict[point], end=' ')