n=int(input())
p=list(map(int,input().split()))
if(len(p)==0):
    print(0)
else:
    mx=0
    mn=p[0]
    for i in range(len(p)):
        profit=p[i]-mn
        mx=max(profit,mx)
        mn=min(mn,p[i])
    print(mx)
    