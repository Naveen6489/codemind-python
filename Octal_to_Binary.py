t=int(input())
for i in range(t):
    s=input()
    g=""
    for i in range(len(s)):
        if(s[i]=="0"):
            g+="000"
        elif s[i]=="1":
            g+="001"
        elif(s[i]=="2"):
            g+="010"
        elif(s[i]=="3"):
            g+="011"
        elif(s[i]=="4"):
            g+="100"
        elif(s[i]=="5"):
            g+="101"
        elif(s[i]=="6"):
            g+="110"
        elif(s[i]=="7"):
            g+="111"
    g=list(g)
    for i in range(len(g)):
        if(g[i]=="1"):
            f=g.index(g[i])
    print("".join(g[f:]))
    
        