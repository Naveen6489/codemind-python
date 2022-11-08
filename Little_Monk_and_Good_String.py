s=input()
a="aeiou"
cnt=0
m=0
for i in range(len(s)):
    if(s[i] in a):
        cnt+=1
    else:
        cnt=0
    if(m<cnt):
        m=cnt
print(m)