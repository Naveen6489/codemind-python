n=int(input())
a=0
b=1
c=[]
while a<=n or b<n:
    c.append(a)
    c.append(b)
    a=a+b
    b=b+a
if n in c:
    print(True)
else:
    print(False)