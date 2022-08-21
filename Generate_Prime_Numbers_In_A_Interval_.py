def prime(n):
    k=n**0.5
    for i in range(2,int(k)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if i<=1:
        continue
        
    if prime(i):
        print(i)