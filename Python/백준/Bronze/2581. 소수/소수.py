import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

result = 0
min_result = 0

for i in range(m,n+1):
    if i < 2:
        continue
    
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        result += i
    
        if min_result == 0: 
            min_result = i

if result == 0:
    print(-1)
else:
    print(result)
    print(min_result)
