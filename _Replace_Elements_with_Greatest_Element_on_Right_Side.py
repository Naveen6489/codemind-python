n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(len(a)-1):
    e=max(a[i+1:])
    c.append(e)
for j in range(len(a)):
    if len(c)!=len(a):
        c.append(-1)
print(*c)