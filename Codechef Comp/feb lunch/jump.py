def sol():
    n,u,d=map(int,input().split())
    dec=False
    dec1=True
    hills=list(map(int,input().split()))
    if n==1:
        print(1)
        return
    position=hills[0]
    for i in range(1,n):
        if position<hills[i]:
            if position+u>=hills[i]:
                position=hills[i]
                continue
            else:
                break
        elif position>hills[i]:
            if position-d<=hills[i]:
                position=hills[i]
                continue
            elif not dec:
                dec=True
                position=hills[i]
            else:
                break
    else:
        dec1=False
        print(i+1)
    if dec1:
        print(i)
    
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
