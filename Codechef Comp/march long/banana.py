def calc(banana,a,mincon):
    temp=0
    for b in banana:
        temp+=(b//mincon)
        if b%mincon!=0:
            temp+=1
        if temp>a:
            return False
    else:
        return True
def sol():
    n,a=map(int,input().split())
    banana=sorted(map(int,input().split()))
    total=sum(banana)
    if total%a!=0:
        mincon=total//a + 1
    else:
        mincon=total//a
    if a<pow(10,7):
        high=banana[-1]
    else:
        high=2*mincon
    low=mincon
    while high>=low:
        mid=(high+low)//2
        if calc(banana,a,mid):
            high=mid-1
        else:
            low=mid+1
        #print(high,low)
    for i in range(max(mid-1,1),mid+3):
        if calc(banana,a,i):
            break
    print(i)
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
