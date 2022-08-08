n=input()
c=[]
m=["a","e","i","o","u"]
for i in range(len(m)):
    if m[i] not in n:
        c.append(m[i])
if len(c)==0:
    print(0)
else:
    print(*c)
        