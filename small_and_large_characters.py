n=input()
k=n.split()
for i in range(len(n)):
    print(min(k[i]),max(k[i]),end=" ")
    