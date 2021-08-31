def balance():
    n,p=map(int,input().split())
    a=list(map(int,input().split()))[:n]
    hard=0
    cake=0
    for l in a:
        if l<=p//10:
            hard+=1
        elif l>=p//2:
            cake+=1
        else:
            continue
    if hard==2 and cake==1:
        return "yes"
    else:
        return "no"
if __name__=="__main__":
    ans=[]
    for _ in range(int(input())):
        ans.append(balance())
    print(*ans,sep="\n")