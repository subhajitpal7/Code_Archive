def somefun():
    n,k=map(int,input().split())
    ans=0
    arr=list(map(int,input().split()))[:n]
    for a in arr:
        if (a+k)%7==0:
            ans+=1
    return ans

if __name__=="__main__":
    ans=[]
    for _ in range (int(input())):
        ans.append(somefun())
    print(*ans)
