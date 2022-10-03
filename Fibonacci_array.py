n=int(input())
m=list(map(int,input().split()))
a=m[0]
b=m[1]
t=True
for i in range(2,n):
    c=a+b
    a=b
    b=c
    if c!=m[i]:
        t=False
        break
if t==True and n>2:
    print("yes")
else:
    print("no")
