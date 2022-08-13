n=int(input())
s=0
while n:
    m=n%10
    s=m*m+s
    n=n//10
    if n==0 and s>9:
        n=s
        s=0
if s==1 or s==7:
    print(True)
else:
    print(False)