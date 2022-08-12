n=input()
m=n.upper()
c=0
for i in n:
    if i not in m:
        c+=1
print(c)
        