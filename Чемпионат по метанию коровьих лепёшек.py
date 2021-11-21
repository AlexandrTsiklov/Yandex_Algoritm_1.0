n, dist = int(input()), list(map(int, input().split()))
max_v, min_v, our_ch = max(dist), min(dist), 0

for i in range(1, len(dist) - 1):
    if dist[i - 1] == max_v and dist[i + 1] == min_v and dist[i] % 10 == 5:
        if dist[i] >= our_ch:
            our_ch = dist[i]

dist.sort(reverse=True)
if our_ch == 0:
    print(our_ch)
else:
    print(dist.index(our_ch) + 1) #
