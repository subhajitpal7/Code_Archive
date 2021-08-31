def fun():
    ans=[]
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))[:n]
    prod=1
    for a in arr:
        prod*=a
    queries=list(map(int,input().split()))[:q]
    for a in queries:
        ans.append(a//prod)
    print(*ans,sep=" ")
if __name__=="__main__":
    for _ in range(int(input())):
        fun()
