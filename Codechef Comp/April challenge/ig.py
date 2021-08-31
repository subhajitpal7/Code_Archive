from collections import defaultdict as dic
def si():
    return input()
def mi():
    return map(int,input().split())
def ii():
    return int(input())
def dfs(no,arv,gems):
    #print(no,end=" ")
    gems[no]+=1
    for a in adj[no]:
        if a!=arv:
            dfs(a,no,gems)
        if a==arv:
            return
def BFS(s,n):
        visited = [False] * (n)
        queue = []
        queue.append(s)
        visited[s] = True
        a=s
        while queue:
            s = queue.pop(0)
            if a in store:
                store[a].append(s)
            else:
                store[a]=[s]
            #print (s, end = " ")
            for i in adj[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
def sol():
    n,m=mi()
    for i in range(n-1):
        a,b=mi()
        a,b=a,b
        if a in adj:
            adj[a].append(b)
        else:
            adj[a]=[b]
        if b in adj:
            adj[b].append(a)
        else:
            adj[b]=[a]
    #for a in adj:
        #BFS(a,n)
    gems=[0]*(n+1)
    for i in range(m):
        a,b=mi()
        a,b=a,b
        dfs(a,b,gems)
    print(max(gems))
        
if __name__=="__main__":
    adj=dic()
    store=dic()
    sol()
