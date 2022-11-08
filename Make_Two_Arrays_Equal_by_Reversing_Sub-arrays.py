n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
cnt=0
if(len(a)==len(b)):
    a.sort()
    b.sort()
    if a==b:
        print(True)
    else:
        print(False)
else:
    print(False)