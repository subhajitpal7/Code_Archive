def sol():
    n=int(input())
    x=[]
    y=[]
    for i in range(n):
        xi,yi=map(int,input().split())
        x.append(xi)
        y.append(yi)
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            if pow(x[i]-x[j],2)+pow(y[i]-y[j],2)==pow(abs(x[i]-x[j])+abs(y[i]-y[j]),2):
                ans+=1
    print(ans)
if __name__=="__main__":
    sol()
