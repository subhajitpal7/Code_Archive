def sieve():
    for i in range(3,301):
        F.append(F[i-2]+F[i-1])

if __name__=="__main__":
    F=[1,2,3,4]
    sieve()
    INF  = 99999
    V,e=map(int,input().split())
    graph=[[INF for i in range(V)] for i in range(V)]
    for i in range(e):
        u,v,w=map(int,input().split())
        graph[u-1][v-1]=w
        graph[v-1][u-1]=w
    for i in range(V):
        graph[i][i]=0
    dist=graph
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j],dist[i][k]+ dist[k][j])
    val=[0 for i in range(V)]
    q=int(input())
    for i in range(q):
        u,k=map(int,input().split())
        temp=dist[u-1]
        for i in range(V):
            val[i]+=temp[i]+F[k]
    mod=1000000009
    for i in range(V):
        val[i]%=mod
    print(*val)
