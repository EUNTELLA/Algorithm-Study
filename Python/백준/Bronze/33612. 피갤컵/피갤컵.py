import sys
input = sys.stdin.readline

n = int(input())

years = 2024
month = 8

month += (n-1) * 7

while month > 12:
    years += 1
    month -= 12

print(years,month)