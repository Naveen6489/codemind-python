n=input()
m=["a","A","e","E","i","I","o","O","u","U"]
c=[]
for i in range(len(n)):
    if n[i] in m and n[i] not in c:
        c.append(n[i])
if len(c)==0:
    print(-1)
else:
    print(*c)