n=input()
res=0
c=0
for i in range(len(n)-1):
    if(n[i]==n[i+1]):
        c+=1
        res=max(res,c)
    else:
        c=0
print(res+1)