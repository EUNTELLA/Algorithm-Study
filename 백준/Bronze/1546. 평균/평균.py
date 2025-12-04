n = int(input())
scores = list(map(int,input().split()))

max_score = max(scores)

if max_score == 0:
    print(0.0)
else:
    adjusted = [(score/max_score)*100 for score in scores]
    print(sum(adjusted)/n)