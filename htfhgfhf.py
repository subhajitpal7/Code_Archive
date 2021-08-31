def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
def twinpair(a):
    k=False
    i=3
    while(a>0):
        k=isPrime(i)==True and isPrime(i+2)==True
        if(k):
            a-=1
        i+=2
    s=str(i)
    return s
for i in range(1,10):
    print(twinpair(i))
