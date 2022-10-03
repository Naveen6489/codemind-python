n=input()
m=n.split()
m=m[::-1]
c=[]
for i in m:
    for j in i:
        c.append(j)
    break
c.sort()
k=c[0]
if k.lower() in n:
    print(k.lower())
else:
    print(k)