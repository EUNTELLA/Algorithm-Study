n = int(input())
papers = []

for _ in range(n):
    x,y = map(int,input().split())
    papers.append((x,y))
    
s = set()

for x,y in papers:
    for i in range(10):
        for j in range(10):
            s.add((x+i,y+j))

result = len(s)
print(result)