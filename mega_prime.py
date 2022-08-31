def prime(n):
    if n==0 or n==1:
        return False
    a=int(n**0.5)
    for i in range(2,a+1):
        
        if n%i==0:
            return False
    return True
n=int(input())
if prime(n)==False:
    print("Not Mega Prime")
elif prime(n):
    while n:
        k=n%10
        n=n//10
        if prime(k):
            f=True
        else:
            f=False
            break
if f==True:
    print("Mega Prime")
else:
    print("Not Mega Prime")