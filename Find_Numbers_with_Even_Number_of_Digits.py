def count(n):
    c=0
    while n:
        k=n%10
        c+=1
        n=n//10
    if(c%2==0):
        return True
    return False
n=int(input())
m=list(map(int,input().split()))
c=0
for i in m:
    if(count(i)):
        c+=1
print(c)
        
    