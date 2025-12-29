import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [input().strip() for _ in range(n)]
result = []

for i in range(n-7):
    for j in range(m-7):
        count_w = 0
        count_b = 0
        
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y) % 2 == 0:
                   if board[x][y] != 'W':
                       count_w += 1
                   if board[x][y] != 'B':
                       count_b += 1      
                else:
                    if board[x][y] != 'B':
                        count_w += 1
                    if board[x][y] != 'W':
                        count_b += 1
                        
        result.append(count_w)
        result.append(count_b)
print(min(result))