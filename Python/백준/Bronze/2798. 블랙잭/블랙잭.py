import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int,input().split()))

result = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            cur_sum = nums[i] + nums[j] + nums[k] 
            
            if cur_sum <=m:
                result = max(result,cur_sum)
                

print(result)