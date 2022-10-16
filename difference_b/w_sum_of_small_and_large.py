n=input()
k=n.split()
a=0
b=0
for i in k:
    c=[]
    for j in i:
        c.append(ord(j))
    a+=max(c)
    b+=min(c)
print(abs(a-b))
    