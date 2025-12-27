import sys
input = sys.stdin.readline

num = [0]*10001

n = int(input())
for _ in range(n):
    nums = int(input())
    num[nums] += 1

for i in range(10001):
    if num[i] !=0:
        for _ in range(num[i]):
            print(i)