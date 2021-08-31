from collections import defaultdict as dic
from random import randint
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q # use x//y for floor "floor division"
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y
def modinv(a, m):
    g, x, y = egcd(a, m) 
    if g != 1:
        return None
    else:
        return x % m
def fac(n, modulus):
    ans=1
    if n <= modulus//2:
        #calculate the factorial normally (right argument of range() is exclusive)
        for i in range(1,n+1):
            ans = (ans * i) % modulus   
    else:
        #Fancypants method for large n
        for i in range(1,modulus-n):
            ans = (ans * i) % modulus
        ans = modinv(ans, modulus)

        #Since m is an odd-prime, (-1)^(m-n) = -1 if n is even, +1 if n is odd
        if n % 2 == 0:
            ans = -1*ans + modulus
    return ans % modulus
def binomial(x, y):
    try:
        binom = fac(x,mod) // fac(x - y,mod)
    except ValueError:
        binom = 0
    return binom%mod
def sol():
    n,w=map(int,input().split())
    w=abs(w)
    print(binomial((n+w-1),n-1))
if __name__=="__main__":
    mod=pow(10,9)+7
    for _ in range(int(input())):
        sol()
