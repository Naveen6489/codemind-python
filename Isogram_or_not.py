m=input()
c=[]
for i in range(len(m)):
    if m[i] not in c:
        c.append(m[i])
if len(c)==len(m):
    print(True)
else:
    print(False)
    