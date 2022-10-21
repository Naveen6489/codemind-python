n=input()
c=0
for i in n:
    if i=="U" or i=="R":
        c+=1
    elif i=="D" or i=="L":
        c-=1
if(c==0):
    print(True)
else:
    print(False)
