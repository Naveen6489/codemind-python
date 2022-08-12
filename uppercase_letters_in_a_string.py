n=input()
m=n.lower()
c=0
for i in range(len(n)):
    if n[i] not in m:
        c+=1
print(c)