n=int(input())
a=list(map(int,input().split()))
up=0
down=0
for i in range(len(a)):
    if(a[i]==1):
        down+=1
    else:
        down=0
    if(up<down):
        up=down
print(up)