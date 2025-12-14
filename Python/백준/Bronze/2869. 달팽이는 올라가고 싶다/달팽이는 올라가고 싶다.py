a, b, v = map(int,input().split())
day = 0

target = v-a
day += a - b

print((target+ day-1)//day + 1)

