n, distances = int(input()), list(map(int, input().split()))
max_v, min_v, our_ch, position = max(distances), min(distances), 0, 1

flag_out, flag_in = False, False
for i in range(1, len(distances) - 1):

    if distances[i - 1] == max_v:
        flag_out = True

    if flag_out is True:
        if distances[i] % 10 == 5 and distances[i + 1] < distances[i]:
            flag_in = True
            if distances[i] > our_ch:
                our_ch = distances[i]

sorted_distances = sorted(distances, reverse=True)
for dist in sorted_distances:
    if dist == our_ch:
        print(position)
        break
    position += 1

if flag_in is False:
    print(0)







