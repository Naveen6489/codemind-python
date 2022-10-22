n=input()
n=str(n)
rev=n[::-1]
rev=int(rev)
s=""
while rev:
    k=rev%10
    if k%2==0:
        s+=""
    else:
        l=k*k
        s+=str(l)
    rev=rev//10
print(s)
    
        
    
    