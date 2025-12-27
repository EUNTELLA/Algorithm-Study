import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

print(round(sum(nums)/n))
print(nums[n//2])

dic = {}
for i in nums:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

max_freq = max(dic.values())
modes = []
for key, value in dic.items():
    if value == max_freq:
        modes.append(key)


if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

print(nums[-1]-nums[0])