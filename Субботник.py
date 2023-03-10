amt_of_students, nessessary_aog, amt_people_in_group = map(int, input().split())  # aog - amount of groups, amt - amount
students_heights = sorted([int(input()) for _ in range(amt_of_students)])


def form_enough_groups(delta):
    first_si, current_aog = 0, 0  # first_si - first student's index 
    while (first_si < amt_of_students) and (current_aog < nessessary_aog):
        last_si = first_si + amt_people_in_group - 1
        if last_si >= amt_of_students:
            break
        elif students_heights[last_si] - students_heights[first_si] > delta:
            first_si += 1
        else:
            first_si = last_si + 1
            current_aog += 1
    return current_aog >= nessessary_aog


l, r = 0, students_heights[-1] - students_heights[0]
while l < r:
    m = (l + r) // 2
    if form_enough_groups(m):
        r = m
    else:
        l = m + 1
print(r)
