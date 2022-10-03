n=int(input())
m=list(map(int,input().split()))
f=False
d=0
c=0
for i in range(1,len(m)-1,2):
    if m[i]>m[i-1] and m[i]>m[i+1]:
        t=True
        c+=1
    elif m[i]<m[i-1] and m[i]<m[i+1]:
        t=True
        c+=1
    else:
        d+=1
if t==True and d==0:
    print(c)
else:
    print(-1)
