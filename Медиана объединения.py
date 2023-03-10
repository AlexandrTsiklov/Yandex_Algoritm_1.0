N, L = map(int, input().split())
sequenses = [list(map(int, input().split())) for _ in range(N)]
for i in range(N - 1):
    for j in range(i + 1, N):
        print((sorted(sequenses[i] + sequenses[j]))[L - 1])
