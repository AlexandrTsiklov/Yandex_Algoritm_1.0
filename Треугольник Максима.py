n = int(input())
lst_music = [list(input().split()) for i in range(n)]
rng_min, rng_max = 30, 4000


for i in range(1, len(lst_music)):
    current_v, last_v = float(lst_music[i][0]), float(lst_music[i - 1][0])
    if (lst_music[i][1] == 'further' and current_v > last_v) \
        or (lst_music[i][1] == 'closer' and current_v < last_v):

        new_rng_max = (current_v + last_v) / 2
        if new_rng_max < rng_max:
            rng_max = new_rng_max

    elif (lst_music[i][1] == 'further' and current_v < last_v) \
        or (lst_music[i][1] == 'closer' and current_v > last_v):

        new_rng_min = (current_v + last_v) / 2
        if new_rng_min > rng_min:
            rng_min = new_rng_min

print('%.7f' % float(rng_min), '%.7f' % float(rng_max))  #



