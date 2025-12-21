n,k = map(int,input().split())
result =0
for i in range(1,n+1):
    if n%i == 0:
        result += 1
        
    if result == k :
        print(i)
        exit()

print(0)