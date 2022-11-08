s=input()
s=list(s)
i=0
j=len(s)-1
while i<=j:
    if(s[i].islower()):
        if(s[j].islower()):
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        else:
            j-=1
    else:
        i+=1
print("".join(s))