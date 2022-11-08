s=input()
a="aeiou"
l=""
for i in range(len(s)):
    if(s[i] in a):
        l+="V"
    else:
        l+="C"
l=list(l)
op=[]
op.append(l[0])
for i in l:
    if(op[-1]!=i):
        op.append(i)
print("".join(op))