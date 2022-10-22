n=input()
k=n.split()
c=[]
rev=(k[::-1])
for i in rev:
    c.append(i)
print(*c)
