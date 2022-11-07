n=int(input())
for i in range(n):
    s=input()
    for i in range(len(s)):
        if(s[i]=="0"):
            print("0000",end="")
        elif(s[i]=="1"):
            print("0001",end="")
        elif(s[i]=="2"):
            print("0010",end="")
        elif(s[i]=="3"):
            print("0011",end="")
        elif(s[i]=="4"):
            print("0100",end="")
        elif(s[i]=="5"):
            print("0101",end="")
        elif(s[i]=="6"):
            print("0110",end="")
        elif(s[i]=="7"):
            print("0111",end="")
        elif(s[i]=="8"):
            print("1000",end="")
        elif(s[i]=="9"):
            print("1001",end="")
        elif(s[i]=="A"):
            print("1010",end="")
        elif(s[i]=="B"):
            print("1011",end="")
        elif(s[i]=="C"):
            print("1100",end="")
        elif(s[i]=="D"):
            print("1101",end="")
        elif(s[i]=="E"):
            print("1110",end="")
        elif(s[i]=="F"):
            print("1111",end="")
        if i==len(s)-1:
            print()
            