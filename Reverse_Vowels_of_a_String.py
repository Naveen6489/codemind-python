n=input()
s=0
s1="aeiouAEIOU"
r=[]
for i in range(len(n)):
    if(n[i] in s1):
        r.append(n[i])
r.reverse()
n=list(n)
for j in range(len(n)):
    if(n[j] in s1):
        n[j]=str(r[s])
        s+=1
print("".join(n))