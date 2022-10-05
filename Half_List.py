n=int(input())
m=list(map(int,input().split()))
k=m[::-1]
c=[]
for i in range(len(k)//2):
    c.append(k[i])
for i in range(len(m)//2):
    c.append(m[i])
print(*c)
    