
n=int(input())
m=list(map(int,input().split()))
c=[]
for i in m:
    c.append(i**2)
c.sort()
print(*c)
