def sol():
    n,k,s=map(int,input().split())
    weeks=s//7
    eb=s-weeks
    if n*eb<s*k or n<k:
        print(-1)
    else:
        ans=s*k
        if ans%n!=0:
            print((ans//n)+1)
        else:
            print(ans//n)

if __name__=="__main__":
    for _ in range(int(input())):
        sol()
