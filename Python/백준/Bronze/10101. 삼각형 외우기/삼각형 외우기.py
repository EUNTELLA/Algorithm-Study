result = []
for _ in range(3):
    result.append(int(input()))

total = sum(result)
if total != 180 :
    print("Error")
else:
    if result[0] == result[1] == result[2]:
        print("Equilateral")
    elif result[0] == result[1] or result[0] == result[2] or result[1]==result[2]:
        print("Isosceles")
    else:
        print("Scalene")
