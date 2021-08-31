def GoodOrBad():
    n,k=map(int,input().split())
    s=input()
    cap=0
    small=0
    for a in s:
        if ord(a) in range(ord('A'),ord('Z')+1):
            cap+=1
        else:
            small+=1
    dec=n-k
    if cap>=dec and small>=dec:
        return "both"
    elif cap>=dec:
        return "brother"
    elif small>=dec:
        return "chef"
    else:
        return "none"
        
if __name__=="__main__":
    for _ in range(int(input())):
        print(GoodOrBad())
