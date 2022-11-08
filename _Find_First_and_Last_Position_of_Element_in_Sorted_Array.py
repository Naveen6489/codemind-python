n=int(input())
s=list(map(int,input().split()))
e=int(input())
r=[]
for i in range(len(s)):
    if s[i]==e:
        r.append(i)
if(len(r)==0):
    print(-1,-1)
else:
    print(r[0],r[-1])