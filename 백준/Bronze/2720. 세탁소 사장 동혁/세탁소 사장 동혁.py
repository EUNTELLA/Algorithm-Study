T = int(input())
for i in range(T):
    c =  int(input())
    for i in [25,10,5,1]:
        print(c// i, end = " ")
        c %= i
    print()