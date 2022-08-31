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
for i in range(int(input())):
    a=int(input())
    k=1
    if g[a]==1:
        print(a)
    else:
        while True:
            if g[a-k]==1:
                print(a-k)
                break
            elif g[a+k]==1:
                print(a+k)
                break
            k+=1