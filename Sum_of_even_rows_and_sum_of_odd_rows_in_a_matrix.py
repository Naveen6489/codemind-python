n,m=map(int,input().split())
ev=0
od=0
for i in range(n):
    a=list(map(int,input().split()))
    if(i%2==0):
        ev+=sum(a)
    else:
        od+=sum(a)
print(ev,od)