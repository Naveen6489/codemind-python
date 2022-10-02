n=input()
k=n.split()
for i in range(len(k)):
    if i%2==0:
        k[i]=k[i][::-1]
    print(k[i],end=" ")
        