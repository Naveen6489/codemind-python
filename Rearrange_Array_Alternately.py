t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    f=[]
    for i in range(len(a)//2):
        f.append(max(a))
        a.remove(max(a))
        f.append(min(a))
        a.remove(min(a))
    f=f+a
    print(*f)