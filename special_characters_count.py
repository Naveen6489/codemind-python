n=input()
s=''
c=0
for i in n:
    if i.isalnum() or i==" ":
        s+=i
        c+=1
print(len(n)-len(s))