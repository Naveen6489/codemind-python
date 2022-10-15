n=int(input())
a=n
l=len(str(n))
summ=0
while(a):
    k=a%10
    summ=summ+(k**l)
    a=a//10
    l-=1
if(n==summ):
    print(True)
else:
    print(False)

    
    
