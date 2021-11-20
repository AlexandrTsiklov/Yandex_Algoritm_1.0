lst_figures = list(map(int, input().split()))

max_top, max_bottom = max(lst_figures[0:2]), min(lst_figures[0:2])
min_near, min_far = max(lst_figures[0:2]), min(lst_figures[0:2])

for i in lst_figures[2:]:
    if i < 0:
        if min_far <= i < min_near:
            min_near = i
        elif i < min_far:
            min_far, min_near = i, min_far
    else:
        if max_bottom < i <= max_top:
            max_bottom = i
        elif i >= max_top:
            max_top, max_bottom = i, max_top

if max_bottom * max_top > min_far * min_near:
    print(max_bottom, max_top)
else:
    print(min_far, min_near)



