def employ():
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))[:n]
    for i in range(k):
        arr.append(max(arr)+1)
    arr.sort()
    return arr[len(arr)//2]
if __name__=="__main__":
    ans=[]
    for _ in range(int(input())):
        ans.append(employ())
    print(*ans,sep="\n")