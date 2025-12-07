n = int(input())
cnt = 0
for _ in range(n):
    a = list(input())
    s = set()
    prev = ''
    ok = True
    
    for ch in a:
        if ch != prev:
            if ch in s :
                ok = False
                break
            s.add(ch)
        prev = ch
    
    if ok:
        cnt += 1

print(cnt)