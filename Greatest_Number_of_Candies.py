n=int(input())
m=list(map(int,input().split()))
k=int(input())
c=[]
for i in m:
    if i+k>=max(m):
        c.append("True")
    else:
        c.append("False")
print(*c)