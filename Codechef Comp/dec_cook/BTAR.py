def BTAR():
    n=int(input())
    l=[a%4 for a in map(int,input().split())]
    ans=0
    if sum(l)%4!=0:
        print(-1)
    else:
        one=l.count(1)
        two=l.count(2)
        three=l.count(3)
        ans+=three
        one-=three
        ans+=one//2
        two-=one//2
        ans+=two//2
        print(ans)
if __name__=="__main__":
    for _ in range(int(input())):
        BTAR()
