n=int(input())
m=list(map(int,input().split()))
c=0
for i in range(len(m)):
    if m[i]%2==0:
        c=i
print(c)