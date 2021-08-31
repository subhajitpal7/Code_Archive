def fun():
    s=input()
    stackA=[]
    acount=0
    deca=0
    ansA=0
    for i in range(len(s)):
        if len(stackA)==0 and s[i]=='A':
            stackA.append(s[i])
            ansA+=1
            deca=1
        elif len(stackA)!=0 and s[i]=='A':
            stackA.pop()
            ansA+=acount
            acount=0
            deca=0
        if deca==1:
            acount+=1
    stackA=[]
    acount=0
    deca=0
    ansB=0
    for i in range(len(s)):
        if deca==1:
            acount+=1
        if len(stackA)==0 and s[i]=='B':
            stackA.append(s[i])
            ansB+=1
            deca=1
        elif len(stackA)!=0 and s[i]=='B':
            stackA.pop()
            ansB+=acount+1
            acount=0
            deca=0
        
    return ' '.join(map(str,[ansA,ansB]))
if __name__=="__main__":
    ans=[]
    for _ in range(int(input())):
        ans.append(fun())
    print(*ans,sep="\n")
