n=int(input())
m=list(map(int,input().split()))
c=[]
d=[]
for i in range(len(m)):
    if m[i]==0:
        c.append(m[i])
    else:
        d.append(m[i])
    
        
print(*c+d)