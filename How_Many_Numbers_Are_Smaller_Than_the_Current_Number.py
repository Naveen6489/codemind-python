n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(len(a)):
    cnt=0
    for j in range(len(a)):
        if a[i]>a[j]:
            cnt+=1
    l.append(cnt)
print(*l)