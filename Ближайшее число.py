n = int(input())
lst = list(map(int, input().split()))
x = int(input())
minimum = 2002
ch = 1001
for i in lst:
    if abs(i - x) <= minimum:
        minimum = abs(i - x)
        ch = i
print(ch)  #
