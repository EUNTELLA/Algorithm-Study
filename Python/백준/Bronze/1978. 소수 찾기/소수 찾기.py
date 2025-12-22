import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
total = 0

for num in arr:
    if num < 2:
        continue
    
    for i in range(2,num):
        if num % i == 0:
            
            break
    else:
        total += 1

print(total)