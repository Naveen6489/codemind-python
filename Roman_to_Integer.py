n=input()
d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
s=d[n[-1]]
for i in range(len(n)-1):
    if(d[n[i]]<d[n[i+1]]):
        s-=d[n[i]]
    else:
        s+=d[n[i]]
print(s)