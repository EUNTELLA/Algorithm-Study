dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

result = 0
word = input()

for spel in dial:
    for i in spel:
        for x in word:
            if i == x:
                result += dial.index(spel)+3
print(result)