def prime(n):
    a=n**0.5
    for i in range(2,int(a)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
m=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(m)):
    if m[i]==1:
        continue
    if m[i]<=k and prime(m[i]):
        c+=1
print(c)