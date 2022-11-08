import collections
n=int(input())
a=list(map(int,input().split()))
l=collections.Counter(a)
a.sort(key=lambda x:(-l[x],x))
p=[]
for i in range(len(a)):
    if a[i] not in p:
        p.append(a[i])
print(*p)