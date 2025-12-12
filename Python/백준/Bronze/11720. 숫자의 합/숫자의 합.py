a = int(input())
sum = 0

list = list(map(int,input()))
for i in range(a):
    sum += list[i]

print(sum)