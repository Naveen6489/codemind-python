import collections
s=input()
s=list(s)
for i in range(len(s)):
    if(s.count(s[i])==1):
        s.pop(i)
        break
s=collections.Counter(s)
res=0
val=list(s.values())[0]
for ele in s:
    if s[ele]!=val:
        res=1
        break
if res==1:
    print("Not Valid")
else:
    print("Valid String")