n=int(input())
d=list(map(int,input().split()))
d.sort()
for i in range(1,d[-1]):
    if i not in d:
        print(i)
        break
else:
    print(d[-1]+1)