l=int(input())
t=int(input())
for i in range(t):
    w,h=map(int,input().split())
    if w==h and w>=l and h>=l:
        print("ACCEPTED")
    elif w<l or h<l:
        print("UPLOAD ANOTHER")
    elif w>l or h>l or w!=h:
        print("CROP IT")
        