n=int(input())
s=""
while n:
    a=n%26
    if a==0:
        s+="Z"
        n=(n//26)-1
    else:
        s+=chr(64+a)
        n=n//26
print(s[::-1])