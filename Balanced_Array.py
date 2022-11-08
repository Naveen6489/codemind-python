t=int(input())
for _ in range(t):
    n=int(input())
    f=list(map(int,input().split()))
    cnt=0
    for i in range(len(f)):
        if(sum(f[:i+1])==sum(f[i:])):
            print("YES")
            cnt+=1
            break
    if(cnt==0):
        print("NO")