def fun():
    n=int(input())
    arr=list(map(int,input().split()))[:n]
    pairs=[]
    for i in range(n):
        for j in range(i+1,n):
            a=arr[i]+arr[j]
            pairs.append(a)
    f=len(pairs)
    l=pairs.count(max(pairs))
    return float("{0:.8f}".format(l/f))
if __name__=="__main__":
    ans=[]
    for _ in range(int(input())):
        ans.append("{0:.8f}".format(fun()))
    print(*ans,sep="\n")
        
