def rec(a,b,arr1,ans,reduce):
    if reduce==0:
        return
    else:
        dec1,dec2,dec3,dec4=0,0,0,0
        if ([a-1,b] not in forbidden) and (a-1 in range(0,n)):
                if arr1[a-1][b]<reduce:
                    arr1[a-1][b]=reduce
                    ans[a-1][b]='Y'
                    #print(arr1[a-1][b])
                    rec(a-1,b,arr1,ans,reduce-1)
        if ([a+1,b] not in forbidden) and (a+1 in range(0,n)):
                if arr1[a+1][b]<reduce:
                    arr1[a+1][b]=reduce
                    ans[a+1][b]='Y'
                    #print(arr1[a+1][b])
                    rec(a+1,b,arr1,ans,reduce-1)
        if ([a,b-1] not in forbidden) and (b-1 in range(0,m)):
                if arr1[a][b-1]<reduce:
                    arr1[a][b-1]=reduce
                    ans[a][b-1]='Y'
                    #print(arr1[a][b-1])
                    rec(a,b-1,arr1,ans,reduce-1)
        if ([a,b+1] not in forbidden) and (b+1 in range(0,m)):
                if arr1[a][b+1]<reduce:
                    arr1[a][b+1]=reduce
                    ans[a][b+1]='Y'
                    #print(ans[a][b+1])
                    rec(a,b+1,arr1,ans,reduce-1)
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().split())
        arr=[]
        escape=[]
        forbidden=[]
        for i in range(n):
            temp=list(map(int,input().split()))
            for j in range(m):
                if temp[j]>0:
                    escape.append([i,j])
                elif temp[j]<0:
                    forbidden.append([i,j])
            arr.append(temp)
        arr1=[[-2]*m for i in range(n)]
        ans=[['N']*m for i in range(n)]
        for i,j in escape:
            arr1[i][j]=arr[i][j]
            ans[i][j]='Y'
        for i,j in forbidden:
            ans[i][j]='B'
            arr1[i][j]=-999
        for [i,j] in escape:
            a,b=i,j
            reduce=arr[a][b]
            rec(a,b,arr1,ans,reduce)
        #print(*arr1,sep='\n')
        for a in ans:
            print(''.join(a))
