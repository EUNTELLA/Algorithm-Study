import sys
input = sys.stdin.readline
n= int(input())
x_list = []
y_list = []
for i in range(n):
    x,y =map(int,input().split())
    x_list.append(x)
    y_list.append(y)

x_result = max(x_list)-min(x_list)
y_result = max(y_list)-min(y_list)

print(x_result * y_result)