def fun():
    n=int(input())
    if n%2==0:
        return n
    else:
        return n-1
    
if __name__=="__main__":
    ans=[]
    for _ in range(int(input())):
        ans.append(fun())
    print(*ans,sep="\n")
