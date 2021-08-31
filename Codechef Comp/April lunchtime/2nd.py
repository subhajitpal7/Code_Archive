from collections import defaultdict as dic
def ii():
    return int(input())
def mi():
    return map(int,input().split())
def si():
    return input()
def sol():
    n=ii()
    adj=dic()
    for i in range(n-1):
        a,b=mi()
        if a in adj:
            adj[a].append(b)
        else:
            adj[a]=[b]
        if b in adj:
            adj[b].append(a)
        else:
            adj[b]=[a]
    #print(adj)
    ans=dic()
    ctr=0
    if n<4 or (n-1)%3!=0:
        print("NO")
        return
    for a in adj:
        if len(adj[a])>=3:
            temp1=adj[a]
            #print("before",temp1)
            for b in ans:
                if b in temp1:
                    temp1.remove(b)
            #print("after",temp1)
            x=len(temp1)
            if x>=3:
                ite=x//3
                j=0
                while ite: 
                    temp=[a,*temp1[j:j+3]]
                    #print(temp)
                    j+=3
                    ite-=1
                    if a in ans:
                        ans[a].append(temp)
                        ctr+=1
                    else:
                        ans[a]=[temp]
                        ctr+=1
    #print(ans)
    if ctr==((n-1)//3):
        print("YES")
        for a in ans:
            for b in ans[a]:
                print(*b)
    else:
        print("NO")
    
if __name__=="__main__":
    for _ in range(ii()):
        sol()
