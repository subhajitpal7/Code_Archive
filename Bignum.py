def fun():
    A,X,N=map(int,input().split())
    if A==0:
        return 0
    else:
        a,b=max(int(str(A)*X),N),min(int(str(A)*X),N)
        return a%b
    
if __name__=="__main__":
    ans=[]
    for _ in range(int(input())):
        ans.append(fun())
    print(*ans,sep="\n")
