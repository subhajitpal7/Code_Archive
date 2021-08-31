def ltor():
    l,r=map(int,input().split())
    while True:
        if l%6==0:
            break
        l+=1
    while True:
        if r%6==0:
            break
        r-=1
    n=(r-l)//6+1
    return (n*(l+r))//2
if __name__=="__main__":
    ans=[]
    for _ in range(int(input())):
        ans.append(ltor())
    print(*ans,sep="\n")
