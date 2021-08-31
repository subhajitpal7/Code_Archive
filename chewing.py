from bisect import bisect as b
def chewing():
    n,k=map(int,input().split())
    hardness=sorted(map(int,input().split()))
    idx=b(hardness,k)
    hardness=hardness[:idx]
    n=len(hardness)
    ans=0
    for i in range(n):
        for j  in range(i+1,n):
            if hardness[i]+hardness[j]<k:
                ans+=1
    print(ans)
if __name__=="__main__":
    chewing()
