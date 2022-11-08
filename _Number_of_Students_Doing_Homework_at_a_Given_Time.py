a=int(input())
l=list(map(int,input().split()))
b=int(input())
l2=list(map(int,input().split()))
c=int(input())
c1=0
for i in range(0,b):
    if l2[i]>=c and l[i]<=c:
        c1+=1
print(c1)
