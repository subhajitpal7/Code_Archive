if __name__=="__main__":
    for _ in range(int(input())):
        base,exp=map(int,input().split())
        res=1
        while exp>0:
            if exp%2==1:
                res=res*base
            base=base*base
            exp//=2
        x = res % 9
        print(x if x else 9)
