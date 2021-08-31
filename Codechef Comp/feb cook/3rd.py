def sol():
    n,k,b=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    a=arr[0]
    ans=0
    for i in range(1,n):
        if a*k+b<=arr[i]:
            ans+=1
            a=arr[i]
    return ans+1
if __name__=="__main__":
    for _ in range(int(input())):
        print(sol())
