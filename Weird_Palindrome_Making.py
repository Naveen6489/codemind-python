t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    od=0
    for i in range(len(l)):
        if l[i]%2:
            od+=1
    if(sum(l)%2==0):
        print(od//2)
    else:
        print((od-1)//2)