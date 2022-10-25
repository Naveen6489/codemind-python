n=int(input())
m=list(map(int,input().split()))
for i in m:
    if m.count(i)>n/2:
        print(i)
        break