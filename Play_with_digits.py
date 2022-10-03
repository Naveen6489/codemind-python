def summ(n):
    s=0
    while n:
        k=n%10
        s+=k
        n=n//10
    return s
n=int(input())
m=list(map(int,input().split()))
k=0
for i in range(len(m)):
    k+=summ(m[i])
print(k)