a, b, c = int(input()), int(input()), int(input())

if c < 0:
    print('NO SOLUTION')
else:
    if a == 0 and b == c**(1/2):
        print('MANY SOLUTIONS')
    elif a != 0:
        print(int((c**2 - b) / a))
    else:
        print('NO SOLUTION')





