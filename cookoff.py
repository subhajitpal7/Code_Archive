def cookoff():
    n=int(input())
    cake=0
    sim=0
    easy=0
    em_m=0
    mh_h=0
    for _ in range(n):
        b=input()
        if b=="cakewalk":
            cake+=1
        elif b=="easy":
            easy+=1
        elif b=="simple":
            sim+=1
        elif b=="easy-medium" or b=="medium":
            em_m+=1
        elif b=="medium-hard" or b=="hard":
            mh_h+=1
        else:
            return None
    if (cake!=1 or easy!=1 or sim!=1) and (em_m<1 or mh_h<1):
        return "No"
    else:
        return "Yes"  
if __name__=="__main__":
    ans=[]
    for _ in range(int(input())):
        ans.append(cookoff())
    print(*ans,sep="\n")
