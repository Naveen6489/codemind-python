n=int(input())
nums=list(map(int,input().split()))
first = nums[:n//2]
se=nums[n//2:]
k=[0]*n
l=0
for i in range(len(first)):
    print(first[i],se[i],end=" ")