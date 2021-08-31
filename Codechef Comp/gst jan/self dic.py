for i in range(int(input())):
    INF  = 99999
    V,m,s,e=map(int,input().split())
    graph=[[INF for i in range(V)] for i in range(V)]
    la=[]
    ra=[]
    for i in range(m):
        u,v=map(int,input().split())
        graph[u-1][v-1]=1
        la.append(u-1)
        ra.append(v-1)
    if s==e:
        print("YES",0)
    elif ((s-1) not in la) or ((e-1) not in ra):
        print("NO")
    else:
        for i in range(V):
            graph[i][i]=0
        dist=graph
        val=0
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    dist[i][j] = min(dist[i][j],dist[i][k]+ dist[k][j])
                    if dist[s-1][e-1]!=INF:
                        val=1
                        print("YES",k)
                        break
                if val==1:
                    break
            if val==1:
                break
        
        if val==0:
            print("NO")

