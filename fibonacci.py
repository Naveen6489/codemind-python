n=int(input())
a=0
b=1
for i in range(0,n):
    fib=a
    print(fib,end=" ")
    a=b
    b=fib+b