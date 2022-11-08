n=int(input())
k=list(map(int,input().split()))
d=1
for i in range(len(k)):
    d*=k[i]
for j in range(len(k)):
    print(d//k[j],end=" ")