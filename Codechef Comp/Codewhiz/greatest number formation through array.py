'''def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac'''
from functools import cmp_to_key as cmp
def mycmp(a, b):
    a, b = str(a), str(b)
    ab, ba = a + b, b + a
    if ab == ba:
        return 0
    if ab < ba:
        return -1
    return 1
def fun():
    n=int(input())
    m=list(map(str,input().split()))
    l=[]
    for a in m:
        for b in a:
            l.append(int(b))
    l=sorted(l,key=cmp(mycmp), reverse=True)
    print(''.join(map(str,l)))
if __name__=="__main__":
    for _ in range(int(input())):
        fun()

