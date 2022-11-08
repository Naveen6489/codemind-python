import collections
n=int(input())
l=list(map(int,input().split()))
c=0
for i in set(l):
    c+=l.count(i)//2
print(c)