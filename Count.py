n=int(input())
m=list(map(int,input().split()))
ev=0
od=0
for i in m:
    if i%2==0:
        ev+=1
    else:
        od+=1
print(ev,od)
    