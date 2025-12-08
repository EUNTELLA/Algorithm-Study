words = []

for _ in range(5):
    words.append(input())

max_len = max(len(w) for w in words)

for i in range(max_len):
    for w in words:
        if i < len(w): 
            print(w[i],end="")