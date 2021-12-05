a = int(input())
b = int(input())
c = int(input())


if a == 0 and b == c * c and c >= 0:
    print('MANY SOLUTIONS')
elif c < 0 or (a == 0 and b != c * c):
    print("NO SOLUTION")
else:
    x = (c**2 - b) / a
    if x.is_integer():
        print(int(x))
    else:
        print('NO SOLUTION')
