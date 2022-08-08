n=input()
m=["a","e","i","o","u"]
for i in range(len(m)):
    if m[i] not in n:
        print(False)
        break
else:
    print(True)