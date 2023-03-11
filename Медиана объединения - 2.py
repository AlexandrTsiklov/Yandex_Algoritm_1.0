def genseq(x1, d1, a, c, m):
    sequence = [x1] * L
    d = d1
    for i in range(1, L):
        sequence[i] = sequence[i - 1] + d
        d = (a * d + c) % m
    return sequence

def lbinsearch(l, r, sequence, x):
    while l < r:
        m = (l + r) // 2
        if sequence[m] < x:
            l = m + 1
        else:
            r = m
    return r

def count_less(sequence, x):
    x_ind = lbinsearch(0, L - 1, sequence, x)
    if sequence[x_ind] < x:
        return L
    return x_ind

def find_median(sequence1, sequence2):
    l = min(sequence1[0], sequence2[0])
    r = max(sequence1[-1], sequence2[-1])
    while l < r:
        m = (l + r + 1) // 2
        c_less = count_less(sequence1, m) + count_less(sequence2, m)
        if c_less < L:
            l = m
        else:
            r = m - 1
    return l

N, L = map(int, input().split())
sequences = [genseq(*map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        print(find_median(sequences[i], sequences[j]))