n=int(input())
cmt=0
arr=n*[None]
for i in range(n):
    arr[i]=int(input())
t=int(input())
for j in range(len(arr)):
    if(arr[j]<=t):
        cmt+=1
    else:
        cmt+=2
print(cmt)