def sol():
    n=int(input())
    arr=sorted(map(int,input().split()))
    ans=0
    for i in range(n-1):
        ans+=arr[i]*arr[i+1]
    print(ans)
if __name__=="__main__":
    sol()
