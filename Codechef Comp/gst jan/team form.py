def grid():
    n=int(input())
    if n==1:
        return int(input())
    ans=0
    for i in range(n):
        l=sorted(map(int,input().split()))
        ans+=abs(l[-1]-l[0])
    return ans
if __name__=="__main__":
    for _ in range(int(input())):
        print(grid())
