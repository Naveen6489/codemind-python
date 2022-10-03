n=input()
m=n.split()
k="aeiouAEIOU"
t=False
c=0
for i in m:
    for j in i:
        if j in k:
            t=True
        if t==False:
            break
        s=i[::-1]
        for z in s:
            if z not in k:
                c+=1
                break
            else:
                break
        break
    t=False
print(c)
            