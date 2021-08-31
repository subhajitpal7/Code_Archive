from collections import Counter as cnt
def sol():
    n=int(input())
    arr=list(map(int,input().split()))
    d=cnt(arr)
    ans=0
    for a in d:
        if d[a]>1:
            ans+=(d[a]*(d[a]-1))//2
    print(ans)
if __name__=="__main__":
    sol()
