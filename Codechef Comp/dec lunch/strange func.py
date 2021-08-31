def f(base, exp,mod):
    res = 1
    while exp > 0:
        if exp % 2 == 1:
            res = (res*base)%mod
        base = (base*base)%mod
        exp //= 2
    return res%mod
if __name__=="__main__":
    for _ in range(int(input())):
        numb,exp=map(int,input().split())
        x=f(numb,exp,9)
        print(x if x else 9)
        
