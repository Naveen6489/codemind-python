def pal(n):
    n=str(n)
    rev=n[::-1]
    rev=int(rev)
    if int(n)==rev:
        return True
    else:
        return False
n=int(input())
k=1
while 1:
    if pal(n+k) and pal(n-k):
        print(n-k,n+k)
        break
    elif pal(n+k):
        print(n+k)
        break
    elif pal(n-k):
        print(n-k)
        break
    k+=1