x = int(input())
k=1

while x > k*(k+1)//2 :
   k += 1

start = k*(k-1)//2
pos = x - start

if k % 2 == 0:
    num = pos
    den = k-pos+1
else: 
    num = k-pos+1
    den = pos

print(f"{num}/{den}")
    