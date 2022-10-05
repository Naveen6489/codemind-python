n=int(input())
m=list(map(int,input().split()))
c=[]
for i in m:
    if m.count(i)==1:
        c.append(i)
if len(c)==0:
    print(-1)
else:
    print(max(c))