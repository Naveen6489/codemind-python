n=input()
k=n.split()
m="aeiou"
c=0
d=[]
for i in k:
    for j in i:
        if j in m:
            c+=1
    d.append(c)
    c=0
print(min(d))