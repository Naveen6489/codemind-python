n,m=map(int,input().split())
ev=0
od=0
for i in range(n):
    a=list(map(int,input().split()))
    for i in range(len(a)):
        if(a[i]%2==0):
            ev+=a[i]
        else:
            od+=a[i]
print(ev,od)