def partition():
    n =int(input())
    arr=list(map(int,input().split()))[:n]
    arr=list(set(arr))
    n=len(arr)
    ansa,ansb=0,0
    if n>=4:
        arr.sort()
        a=arr[:n//2]
        b=arr[n//2:]
        for i in range(n//2-1,0,-1):
            ansa+=i*a[i]-(n//2-1-i)*a[i]
            ansb+=i*b[i]-(n//2-1-i)*b[i]
        ans=ansa+ansb
    elif n==2:
        ans=abs(arr[0]-arr[1])
    elif n==3:
        ans=abs(arr[0]-arr[1])+abs(arr[1]-arr[2])
    return ans
if __name__=="__main__":
    ans=[]
    for _ in range(int(input())):
        ans.append(partition())
    print(*ans,sep="\n")
