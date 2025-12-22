import sys
input = sys.stdin.readline

while True:
    n = int(input())
    result = []
    total = 0
    if n == -1:
        break
    
    for i in range(1,n):
        if n%i == 0:
            result.append(i)
            total += i

    if total == n:
        print(n,"=",end=" ")

        for i in range(len(result)):
            if i == len(result)-1:
                print(result[i])
            else:
                print(result[i],"+",end=" ")
    else:
        print(n,"is NOT perfect.")