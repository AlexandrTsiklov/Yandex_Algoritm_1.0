lst_figures = list(map(int, input().split()))
fst_3_fig = sorted(lst_figures[0:3])

min_near, min_far = fst_3_fig[1], fst_3_fig[0]
otr_near, otr_aver, otr_far = fst_3_fig[2], fst_3_fig[1], fst_3_fig[0]
max_near, max_aver, max_far = fst_3_fig[0], fst_3_fig[1], fst_3_fig[2]

for i in lst_figures[3:]:
    if i < 0:

        if min_far <= i < min_near:
            min_near = i
        elif i <= min_far:
            min_far, min_near = i, min_far

        if i >= otr_near:
            otr_near, otr_aver, otr_far = i, otr_near, otr_aver
        elif i >= otr_aver:
            otr_aver, otr_far = i, otr_aver
        elif i > otr_far:
            otr_far = i

    else:
        if i >= max_far:
            max_far, max_aver, max_near = i, max_far, max_aver
        elif i >= max_aver:
            max_aver, max_near = i, max_aver
        elif i > max_near:
            max_near = i

p1 = max_far * min_near * min_far
p2 = max_near * max_aver * max_far
p3 = otr_far * otr_aver * otr_near
mx = max([p1, p2, p3])

if mx == p1:
    print(max_far, min_near, min_far)
elif mx == p2:
    print(max_near, max_aver, max_far)
else:
    print(otr_far, otr_aver, otr_near)  #