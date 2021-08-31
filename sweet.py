def sweet(L):
    count=0
    l,r=map(int,input().split())
    left,right=L.index(l),L.index(r)
    flagl,flagr=0,0
    if(left-1<0):
        flagl=1
    if(right+1>=n):
        flagr=1
    if flagl==1 and flagr==1:
        count=sum(L[left:right+1])
        for i in range(l,r+1):
            try:
                L.remove(i)
            except:
                continue
    elif flagl==1 and flagr==0:
        count=sum(L[left:right+2])
        for i in range(l,r+2):
            try:
                L.remove(i)
            except:
                continue
    elif flagl==0 and flagr==1:
        count=sum(L[left-1:right+1])
        for i in range(l-1,r+1):
            try:
                L.remove(i)
            except:
                continue
    else:
        count=sum(L[left-1:right+2])
        for i in range(l-1,r+2):
            try:
                L.remove(i)
            except:
                continue
    return count
if __name__=="__main__":
    ans=[]
    n,q=map(int,input().split())
    L=[i for i in range(n)]
    for _ in range(q):
        print(L)
        ans.append(sweet(L))
    print(*ans,sep="\n")