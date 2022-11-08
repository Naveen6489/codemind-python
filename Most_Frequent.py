n=int(input())
a=list(map(int,input().split()))
a.sort()
cnt=0
m=0
for i in range(len(a)):
    if a.count(a[i])>cnt:
        cnt=a.count(a[i])
        m=a[i]
print(m)