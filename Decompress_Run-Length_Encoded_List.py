n=int(input())
a=list(map(int,input().split()))
c=[]
d=[]
for i in range(n):
    if i%2==0:
        c.append(a[i])
    else:
        d.append(a[i])
h=[]
for j in range(len(c)):
    for z in range(c[j]):
        h.append(d[j])
print(*h)