from collections import defaultdict as dic
def sol1():
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    D=list(map(int,input().split()))
    B=list(map(int,input().split()))
    yo=dic()
    for i in range(n):
        if A[i] in yo:
            yo[A[i]]+=D[i]
        else:
            yo[A[i]]=D[i]
    cheflist=sorted(yo.keys(),reverse=True)
    #print(cheflist)
    ans=0
    for i in range(k):
        templist=[]
        if i%2==0:
            choose=B[i]
            for a in cheflist:
                if choose>=yo[a]:
                    choose-=yo[a]
                    if i==k-1:
                        ans+=(yo[a]*a)
                    templist.append(a)
                    #print(a)
                elif choose>0:
                    yo[a]-=choose
                    if i==k-1:
                        ans+=(choose*a)
                    choose=0
                    templist.append(a)
                    break
            cheflist=templist[::-1]
            #print(cheflist)
        else:
            choose=B[i]
            for a in cheflist:
                if choose>=yo[a]:
                    choose-=yo[a]
                    if i==k-1:
                        ans+=(yo[a]*a)
                    templist.append(a)
                elif choose>0:
                    yo[a]-=choose
                    if i==k-1:
                        ans+=(choose*a)
                    choose=0
                    templist.append(a)
                    break
            cheflist=templist[::-1]
            #print(cheflist)
        
    print(ans)

def sol():
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    D=list(map(int,input().split()))
    B=list(map(int,input().split()))
    yo=dic()
    for i in range(n):
        if A[i] in yo:
            yo[A[i]]+=D[i]
        else:
            yo[A[i]]=D[i]
    '''
    cheflist=sorted(yo.keys(),reverse=True)
    chefulist=sorted(yo.keys())
    for i in range(k):
        reformedyo=dic()
        if i%2==0:
            choose=b[i]
            for a in cheflist:
                if choose>yo[a]:
                    choose-=yo[a]
                if '''
    
    for i in range(k):
        if i%2==0:
            A=A[-B[i]:]
        else:
            A=A[:B[i]]
    print(sum(A))
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
