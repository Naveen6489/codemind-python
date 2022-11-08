n=int(input())
for i in range(n):
    a=int(input())
    b=list(map(int,input().split()))
    print(a*(a+1)//2-sum(b))