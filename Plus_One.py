n=int(input())
m=list(map(int,input().split()))
s=""
for i in m:
    s+=str(i)
k=int(s)+1
l=[x for x in str(k)]
print(*l)