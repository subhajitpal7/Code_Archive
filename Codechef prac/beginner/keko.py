def ancmemset(chi,par):
    ancestor[chi]=[ '' for i in range(len(ancestor[par])+1)]
    ancestor[chi][0]=par
    i=0
    while i<len(ancestor[par]):
        ancestor[chi][i+1]=ancestor[par][i]
        i+=1
    for node in Tree[chi]:
        if node!=par:
            ancmemset(node,chi)
def sol(chi,par,maxval):
    if mem[chi][maxval]!=-1:
        return mem[chi][maxval]
    ans=1
    for node in Tree[chi]:
        if node!=par:
            ans+=sol(node,chi,maxval+1)
    if r[chi]>=r[ancestor[chi][maxval]]:
        take=0
        for node in Tree[chi]:
            if node!=par:
                take+=sol(node,chi,0)
        ans=min(ans,take)
    mem[chi][maxval] = ans
    return ans
if __name__=="__main__":
    n=int(input())
    r=[0]
    for a in list(map(int,input().split())):
        r.append(a)
    mem = [[] for i in range(n+1)]
    Tree=[[] for i in range(n+1)]
    ancestor=[[] for i in range(n+1)]
    for j in range(n-1):
        x,y=map(int,input().split())
        Tree[x].append(y)
        Tree[y].append(x)
    ancestor[0].append(0)
    ancmemset(1,0)
    for i in range(n+1):
        mem[i]=[-1 for i in range(len(ancestor[i]))]
    print(sol(1,0,0))
    
