import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True
n=int(input())
l=[]
cnt=0
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
g=[]
for j in range(len(l)):
    if isprime(l[j]):
        g.append(l[j])
for z in range(len(g)-1):
    if g[z]*g[z+1]==n:
        print(g[z],g[z+1])
        cnt=1
if cnt==0:
    print(-1)