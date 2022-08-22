n=int(input())
m=list(map(int,input().split()))
c=[]
s=[]
for i in range(len(m)):
    if m[i] not in c:
        c.append(m[i])
for i in range(len(c)):
    if m.count(c[i])==c[i]:
        s.append(c[i])
if len(s)==0:
    print(-1)
else:
    print(*s)