a,b=map(int,input().split())
x=[]
ev=0
od=0
for i in range(a):
    x.append(list(map(int,input().split())))
for i in range(len(x)):
    for j in range(len(x[i])):
        p=x[i][j]
        if p%2==0:
            ev+=p
        else:
            od+=p
print(ev,od)