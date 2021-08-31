from collections import Counter as cnt
def sol():
    n=int(input())
    arr=list(map(int,input().split()))
    d=cnt(arr)
    ans=0
    for a in d:
        ans+=d[a]-1
    print(ans)
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
