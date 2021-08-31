def sol():
    n,k=map(int,raw_input().split())
    arr=sorted(map(int,raw_input().split()))
    temp1,temp2=arr[1]-arr[0],arr[1]+arr[0]
    for i in xrange(1,n-1):
        if arr[i+1]-arr[i]<temp1:
            if temp1*temp2>(arr[i+1]-arr[i])*(arr[i]+arr[i+1]):
                temp1=arr[i+1]-arr[i]
                temp2=arr[i]+arr[i+1]
    ans=pow(temp1,k,mod)*pow(temp2,k,mod)
    print ans%mod
if __name__=="__main__":
    mod=pow(10,9)+7
    for _ in xrange(int(input())):
        sol()
