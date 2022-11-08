MAX=100
def largestlnCoulumn(mat,rows,cols):
    for i in range(cols):
        maxm=mat[0][i]
        for j in range(rows):
            if mat[j][i]>maxm:
                maxm=mat[j][i]
        print(maxm)
n,m=map(int,input().split())
a=[]
for _ in range(n):
    f=list(map(int,input().split()))
    a.append(f)
largestlnCoulumn(a,n,m);
        