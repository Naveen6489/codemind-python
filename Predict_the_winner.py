n=int(input())
a=list(map(int,input().split()))
l=0
r=0
for i in range(len(a)):
    if i%2==0:
        l+=a[i]
    else:
        r+=a[i]
if abs(l-r)%4==0:
    print("X")
else:
    print("Y")