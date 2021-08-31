if __name__=="__main__":
    n=int(input())
    h=list(map(int,input().split()))
    for i in range(int(input())):
        x,y=map(int,input().split())
        ans=0
        for k in range(1,n+1):
            if k&x==k and h[k-1]>0:
                h[k-1]-=y
                if h[k-1]<=0:      
                    ans+=1
        n-=ans
        print(n)
    
