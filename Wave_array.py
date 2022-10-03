n=int(input())
m=list(map(int,input().split()))
f=False
c=0
d=0
for i in range(1,len(m)-1):
    if m[i]>m[i-1] and m[i]>m[i+1]:
        t=True
        c+=1
    elif m[i]<m[i-1] and m[i]<m[i+1]:
        t=True
        c+=1
    else:
        d+=1
if d==0:
    print("yes")
else:
    print("no")
