x_list = []
y_list = []

for i in range(3):
    x, y = (map(int,input().split()))
    x_list.append(x)
    y_list.append(y)


#
# if x_list[0] == x_list[1]:
#     target_x = x_list[2]
# elif x_list[0] == x_list[2]:
#     target_x = x_list[1]
# else :
#     target_x = x_list[0]
#
# if y_list[0] == y_list[1]:
#     target_y = y_list[2]
# elif y_list[0] == y_list[2]:
#     target_y = y_list[1]
# else:
#     target_y = y_list[0]

for x in x_list:
    if x_list.count(x) == 1:
        target_x = x
for y in y_list:
    if y_list.count(y) == 1:
        target_y = y

print(target_x,target_y)
