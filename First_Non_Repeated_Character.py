n=int(input())
for i in range(n):
    x=int(input())
    m=input()
    for i in m:
        if m.count(i)==1:
            print(i)
            break
    else:
        print(-1)