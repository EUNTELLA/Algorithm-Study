n , m = map(int,input().split())

list_a = [list(map(int,input().split())) for _ in range(n)] 
list_b = [list(map(int,input().split())) for _ in range(n)] 

for i in range(n):
    for j in range(m):
        print(list_a[i][j] + list_b[i][j], end = " ")
    print()