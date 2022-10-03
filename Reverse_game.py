def rev(n):
    n=str(n)
    re=n[::-1]
    return int(re)
n=int(input())
m=list(map(int,input().split()))
c=[]
for i in range(len(m)):
    c.append(rev(m[i]))
print(*c)
    