n=input()
k=n.split()
c=0
m=["a","e","i","o","u",]
for i in k:
    for j in i:
        if j in m:
            c+=1
    print(c,end=" ")
    c=0