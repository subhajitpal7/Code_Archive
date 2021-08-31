def sol():
    n,m=map(int,input().split())
    arr=[]
    for i in range(n):
        a=list(map(int,input().split()))
        arr.append(a)
    if arr[0][0]==-1:
        arr[0][0]=1
    for i in range(n):
        for j in range(m):
            if arr[i][j]==-1 and j==0 and i!=0:
                arr[i][j]=arr[i-1][j]
            elif arr[i][j]==-1 and i==0:
                arr[i][j]=arr[i][j-1]
            elif arr[i][j]==-1:
                arr[i][j]=max(arr[i-1][j],arr[i][j-1])
    for i in range(n):
        for j in range(m-1):
            if arr[i][j]>arr[i][j+1]:
                print(-1)
                return
    for j in range(m):
        for i in range(n-1):
            if arr[i+1][j]!=-1 and arr[i][j]>arr[i+1][j]:
                print(-1)
                return
    else:
        for i in range(n):
            print(*arr[i])
if __name__=="__main__":
    for i in range(int(input())):
        sol()
