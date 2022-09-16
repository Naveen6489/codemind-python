n,k=map(int,input().split())
m=list(map(int,input().split()))
c=0
for i in range(len(m)):
    h=0
    for j in range(i,len(m)):
        h+=m[j]
        if h==k:
            c+=1
print(c)