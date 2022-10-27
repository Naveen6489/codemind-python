n=int(input())
c=[]
d=[]

for i in range(n):
        a=list(map(int,input().split()))
        c.append(a)
for i in range(n):
        a=list(map(int,input().split()))
        e=[]
        for j in range(len(a)):
            e.append(abs(a[j]-c[i][j]))
        print(*e)
            
            
        
    