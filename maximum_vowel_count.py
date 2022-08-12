n=input()
k=n.split()
c=[]
d=0
m="aeiou"
for i in k:
    for j in i:
        if j in m:
            d+=1
    c.append(d)
    d=0
print(max(c))