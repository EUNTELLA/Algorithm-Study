import sys
input = sys.stdin.readline

n,m = map(int,input().split())
c = int(input())
n0 = int(input())

fn_n0 = (n*n0) + m
cgn_n0 = c*n0

if fn_n0 <= cgn_n0 and n <= c:
    print(1)
else:
    print(0)