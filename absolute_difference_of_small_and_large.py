n=input()
k=n.split()
for i in k:
    c=[]
    for j in i:
        c.append(ord(j))
    print(abs(max(c))-min(c),end=" ")
