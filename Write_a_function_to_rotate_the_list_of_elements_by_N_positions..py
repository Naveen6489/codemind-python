a=int(input())
a=list(map(int,input().split()))
k=int(input())
for i in range(k):
    a.insert(0,a[-1])
    a.pop()
print(*a)