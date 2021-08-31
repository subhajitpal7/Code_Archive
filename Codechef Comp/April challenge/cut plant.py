def sol():
    n=int(raw_input())
    garden=list(map(int,raw_input().split()))
    queen=list(map(int,raw_input().split()))
    store=[]
    a=[]
    for i in range(n):
        b=garden[i]-queen[i]
        if b<0:
            return -1
        elif b==0:
            store.append(a)
            a=[]
        else:
            a.append(queen[i])
    if a!=[]:
        store.append(a)
    ans=0
    for a in store:
        ans+=len(set(a))
    change=0
    for i in range(n-1):
        if queen[i]!=queen[i+1]:
            change+=1
    return min(ans,change)
if __name__=="__main__":
    for _ in range(int(raw_input())):
        print(sol())
