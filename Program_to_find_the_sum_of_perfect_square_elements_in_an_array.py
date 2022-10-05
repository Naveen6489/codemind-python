def sqr(n):
    if n==1:
        return True
    for i in range(1,n//2+1):
        if i*i==n:
            return True
    return False
n=int(input())
m=list(map(int,input().split()))
s=0
for i in m:
    if sqr(i):
        s+=i
print(s)
    