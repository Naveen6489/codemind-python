n=input()
k=n.split()
c=[]
for i in k:
    rev=i[::-1]
    c.append(rev)
print(*c)
    