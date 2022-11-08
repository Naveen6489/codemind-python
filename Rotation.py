t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    d=list(map(int,input().split()))
    for i in range(b):
        d.insert(0,d[-1])
        d.pop()
    print(*d)