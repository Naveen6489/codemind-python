t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    a1=list(map(int,input().split()))
    b1=list(map(int,input().split()))
    a1=a1+b1
    a1.sort()
    print(*a1)