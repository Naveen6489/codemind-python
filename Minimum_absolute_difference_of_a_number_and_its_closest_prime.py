def gen_seive():
    dic={}
    for i in range(1000000+1):
        dic[i]=1
    dic[0]=0
    dic[1]=0
    for i in range(2,1000+1):
        if dic[i]==1:
            for j in range(i*i,1000000+1,i):
                dic[j]=0
    return dic
    
        
        
g=gen_seive()
n=int(input())
k=1
if g[n]==1:
    print(0)
else:
    while True:
        if g[n-k]==1:
            print(k)
            break
        elif g[n+k]==1:
            print(k)
            break
        k+=1