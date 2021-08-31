def fun():
    ans=[]
    s=input()
    i=0
    n=len(s)
    ansA=0
    ansB=0
    locansA=0
    locansB=0
    flagA=0
    flagB=0
    while i<n:
        flagA=0
        flagB=0
        if s[i]=='A':
            ansA+=1
            a=i+1
            while a<n:
                if s[a]=='B':
                    locansA=0
                    break
                elif s[a]=='A':
                    flagA=a
                a+=1
            if flagA!=0:
                locansA=flagA-i+1
                ansA+=locansA
                locansA=0
        elif s[i]=='B':
            ansB+=1
            j=i+1
            while(j<n):
                if s[j]=='A':
                    locansB=0
                    break
                elif s[j]=='B':
                    flagB=j
                j+=1
            if flagB!=0:
                locansB=flagB-i+1
                ansB+=locansB
                locansB=0
            
        i+=1
    ans=[ansA,ansB]
    return ans
    
if __name__=="__main__":
    ans=[]
    for _ in range(int(input())):
        ans.append(fun())
    for i in ans:
        print(*i,sep=" ")
        
