def sol():
    n,q=map(int,input().split())
    for i in range(q):
        s=input()
        if len(s)>n:
            print(0)
        else:
            exp=n-len(s)
            ans=pow(26,exp,mod)
            print((ans*(exp+1))%mod)
if __name__=="__main__":
    mod=pow(10,9)+7
    for i in range(int(input())):
        print("Case "+str(i+1)+":")
        sol()
