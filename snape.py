def fun():
    a,b=map(int,input().split())
    ans=[str(round(abs(a**2-b**2)**.5,5)),str(round(abs(a**2+b**2)**.5,5))]
    return " ".join(map(str,ans))
    
if __name__=="__main__":
    ans=[]
    for _ in range(int(input())):
        ans.append(fun())
    print(*ans,sep="\n")
