s=input()
c=0
l=[]
l1=[]
k="[@_!$%()^]<>?\/|}{#&*.:;"
for i in s:
    if i in k:
        c+=1
    elif(i.isdigit()):
        if(int(i)%2==0):
            l.append(i)
        else:
            l1.append(i)
if(c%2==0):
    if(len(l)<len(l1)):
        for i in range(len(l)):
            print(l[i],l1[i],sep="",end="")
        print(*l1[len(l):],sep="")
    else:
        for i in range(len(l1)):
            print(l[i],l1[i],sep="",end="")
        print(*l[len(l1):],sep="")
else:
    if(len(l)<len(l1)):
        for i in range(len(l)):
            print(l1[i],l[i],sep="",end="")
        print(*l1[len(l):],sep="")
    else:
        for i in range(len(l1)):
            print(l1[i],l[i],sep="",end="")
        print(*l[len(l1):],sep="")

        