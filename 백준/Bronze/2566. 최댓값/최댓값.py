max_val = -1
max_j = 0
max_i = 0

for i in range(9):
    nums = list(map(int,input().split()))
    for j in range(9):
        if nums[j] > max_val:
            max_val = nums[j]
            max_i = i + 1
            max_j = j + 1


print(max_val)
print(max_i,max_j)