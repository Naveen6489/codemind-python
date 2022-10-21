for i in range(int(input())):
    
    n=input()
    c=0
    for i in n:
        if i.isdigit():
            c+=1
    if c==0:
        print("No")
    else:
        print("Yes")