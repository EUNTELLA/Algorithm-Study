sides = sorted(list(map(int, input().split())))
a, b, c = sides[0], sides[1], sides[2]

if a + b > c:
    print(a + b + c)
else:
    print((a + b) + (a + b - 1))