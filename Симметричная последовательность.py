n, lst_figures = int(input()), list(map(int, input().split()))
length = len(lst_figures)
i, start, end = -1, length // 2 + length % 2, length // 2

if lst_figures == lst_figures[::-1]:
    print(0)
else:
    lst_figures.append(lst_figures[0])
    while lst_figures[0:start] != lst_figures[-1:end - 1:-1]:
        lst_figures.insert(i, lst_figures[abs(i)])
        start, end = len(lst_figures) // 2 + len(lst_figures) % 2, len(lst_figures) // 2
        i -= 1
    print(len(lst_figures[length:]))
    print(*lst_figures[length:])  #