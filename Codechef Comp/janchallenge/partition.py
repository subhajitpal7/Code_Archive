def checksum(sumleft,k):
    r=True
    for i in range(k):
        if(sumleft[i]!=0):
            r=False
    return r
def subsetsum(S,n,sumleft,A,k):
    if checksum(sumleft,k):
        return True
    if n<0:
        return False
    res=False
    for i in range(k):
        if not res and (sumleft[i]-S[n])>=0:
            A[n]=i+1
            sumleft[i]=sumleft[i]-S[n]
            res=subsetsum(S,n-1,sumleft,A,k)
            sumleft[i]=sumleft[i]+S[n]
    return res
def partition(S,n,k):
    if n<k:
        return "impossible"
    sum1=sum(S)
    A=[0]*n
    sumleft=[0]*k
    for i in range(k):
        sumleft[i]=sum1//k
    res= not (sum1%k) and subsetsum(S,n-1,sumleft,A,k)
    if(not res):
        return "impossible"
    val=0
    for i in range(k):
        for j in range(n):
            if(A[j]==i+1 and val==0):
                ans1.append(S[j])
            elif A[j]==i+1 and val==1:
                ans2.append(S[j])
        val=1
            
if __name__=="__main__":
    for _ in range(int(input())):
        x,n=map(int,input().split())
        S=[i for i in range(1,n+1)]
        ans1=[]
        ans2=[]
        s=['']*n
        s[S.index(x)]='2'
        S.remove(x)
        if partition(S,len(S),2)=="impossible":
            print("impossible")
        else:
            if 1 in ans1:
                for a in ans1:
                    s[a-1]='0'
                for a in ans2:
                    s[a-1]='1'
            else:
                for a in ans2:
                    s[a-1]='0'
                for a in ans1:
                    s[a-1]='1'
            print(''.join(s))
    
