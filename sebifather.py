def sebi():
    s,sg,fg,d,t=map(int,input().split())
    ans=(d*50)/t
    ans*=3.6
    ans+=s
    if abs(sg-ans)==abs(fg-ans):
        return "DRAW"
    elif abs(sg-ans)>abs(fg-ans):
        return "FATHER"
    else:
        return "SEBI"
    
if __name__=="__main__":
    ans=[]
    for _ in range(int(input())):
        ans.append(sebi())
    print(*ans,sep="\n")