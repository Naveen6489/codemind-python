n=int(input())
c=[]
for i in range(1,n+1):
    a,b=map(int,input().split())
    c.append(a+b)
for i in c:
    print(i)