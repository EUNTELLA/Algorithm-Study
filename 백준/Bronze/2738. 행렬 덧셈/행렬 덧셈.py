x,y = map (int,input().split())

x_list , y_list=[] ,[]

for i in range(x):
    a = list(map (int,input().split()))
    x_list.append(a)

for i in range(x):
    b = list(map (int,input().split()))
    y_list.append(b)

for i in range(x):
    for j in range(y):
        print(x_list[i][j] + y_list[i][j], end =' ')
    print()
