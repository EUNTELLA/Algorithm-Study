import sys
input = sys.stdin.readline

n = int(input())
answer =0

for i in range(1,n+1):
    result = i + sum(map(int,str(i)))

    if result == n:
        answer = i
        break
                
print(answer)