def maxsub(arr):
    n=len(arr)
    mxsum=-1e8
    currsum=0
    for i in range(0,n):
        currsum=currsum+arr[i]
        if currsum >mxsum:
            mxsum=currsum
        if(currsum<0):
            currsum=0
    return mxsum
n=int(input())
a=list(map(int,input().split()))
print(maxsub(a))