from time import clock
def f(base, exp,mod):
    res = 1
    while exp > 0:
        if exp % 2 == 1:
            res = (res*base)%mod
        base = (base*base)%mod
        exp //= 2
    return res%mod
a,b,mod=map(int,input().split())
start1=clock()
f(a,b,mod)
end1=clock()
print(end1-start1)
start=clock()
pow(a,b,mod)
end=clock()
print(end-start)
