from collections import Counter as cnt
def sol():
    n=int(input())
    s=''
    for i in range(n):
        s+=input().strip()
    l=input().strip()
    if len(s)>len(l):
        print(-1)
        return
    toch=cnt(s)
    ch=cnt(l)
    l1=sorted(toch)
    l2=sorted(ch)
    deficit=0
    for a in l1:
        if a in ch:
            if ch[a]>=toch[a]:
                ch[a]-=toch[a]
            else:
                deficit+=toch[a]-ch[a]
                toch[a]-=ch[a]
                ch[a]=0
        else:
            deficit+=toch[a]
    temp=deficit
    for a in l2:
        if ch[a]>0:
            temp-=ch[a]
        if temp<=0:
            break
    else:
        print(-1)
        return
    print(deficit)
if __name__=="__main__":
    sol()
    
    
