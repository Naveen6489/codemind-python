n,m=map(int,input().split())
c=0
for i in range(n):
    a=list(map(int,input().split()))
    c+=sum(a)
print(c)