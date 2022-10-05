n=int(input())
m=list(map(int,input().split()))
c=[]
for i in m:
    if i in m and i not in c:
        c.append(i)
print(*c)