lst = list()
count = 0
flag_CONSTANT = True
flag_ASCENDING = True
flag_WEAKLY_ASCENDING = True
flag_DESCENDING = True
flag_WEAKLY_DESCENDING = True

before = int(input())
while True:
    current = int(input())
    if current == -2 * 10**9:
        break
    if current != before:
        flag_CONSTANT = False
    if current <= before:
        flag_ASCENDING = False
    if current < before:
        flag_WEAKLY_ASCENDING = False
    if current >= before:
        flag_DESCENDING = False
    if current > before:
        flag_WEAKLY_DESCENDING = False

    before = current

d = {
    'CONSTANT': flag_CONSTANT,
    'ASCENDING ': flag_ASCENDING,
    'WEAKLY ASCENDING': flag_WEAKLY_ASCENDING,
    'DESCENDING': flag_DESCENDING,
    'WEAKLY DESCENDING': flag_WEAKLY_DESCENDING
}

flag = False
for i in d:
    if d[i] is True:
        print(i)
        flag = True
        break

if flag is False:
    print('RANDOM')
