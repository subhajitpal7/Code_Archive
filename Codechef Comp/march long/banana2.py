def sol():
    n,a=map(int,input().split())
    banana=sorted(map(int,input().split()))
    total=sum(banana)
    if total%a!=0:
        mincon=total//a + 1
    else:
        mincon=total//a
    while True:
        temp=0
        minmod=0
        val=False
        for b in banana:
            temp+=(b//mincon)
            if b%mincon!=0:
                temp+=1
                if b%mincon>minmod and not val:
                    minmod=b%mincon
                    val=True
            if temp>a:
                break
        else:
            break
        mincon+=minmod
    print(mincon)
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
