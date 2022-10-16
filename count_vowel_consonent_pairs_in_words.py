n=input()
k=n.split()
l="aeiouAEIOU"
c=0
z=""
for i in k:
    s=i
    m=len(s)
    rev=i[::-1]
    for j in range(m//2):
        a=s[j]
        b=rev[j]
        if a in l and b not in l:
            if b not in z:
                c+=1
        if a not in l and b in l:
            if a not in z:
                c+=1
print(c)