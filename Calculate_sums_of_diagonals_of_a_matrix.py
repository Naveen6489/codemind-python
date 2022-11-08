n=int(input())
a=[]
for i in range(n):
    f=list(map(int,input().split()))
    a.append(f)
va=0
d=0
for j in range(len(a)):
    for z in range(len(a)):
        if(j==z):
            va+=a[j][z]
            
        if(j+z)==n-1:
            d+=a[j][z]
print("Principal Diagonal:",end="")
print(va)
print("Secondary Diagonal:",end="")
print(d)