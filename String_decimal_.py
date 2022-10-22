x=int(input())
for i in range(x):
    n=input()
    k=len(n)
    c=0
    for i in n:
        if i.isdigit():
            c+=1
    if(k==c):
        print(True)
    else:
        print(False)