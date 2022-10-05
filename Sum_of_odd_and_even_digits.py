n=int(input())
m=list(map(int,input().split()))
ev=0
od=0
for i in range(len(m)):
    if i==0:
        ev+=m[i]
    elif i%2==0:
        ev+=m[i]
    else:
        od+=m[i]
if ev-od==0:
    print("YES")
else:
    print("NO")