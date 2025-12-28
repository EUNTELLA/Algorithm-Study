re = int(input())
while True:
    operators = input()
    if operators == '=':
        break
    n= int(input())
    if operators == '+' :
        re +=n
    elif operators == '-' :
        re -=n
    elif operators == '*' :
        re *= n
    elif operators == '/' :
        re //=n

print(re)