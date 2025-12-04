num1, num2 = input().split()

re_num1 = int(num1 [::-1])
re_num2 = int(num2 [::-1])

print(max(re_num1,re_num2))
