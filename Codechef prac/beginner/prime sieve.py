from bisect import bisect as bs
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
if __name__=="__main__":
    primes=get_primes(1000000)
    for _ in range(int(input())):
        a,b=map(int,input().split())
        idx1=bs(primes,a)
        idx2=bs(primes,b)
        if idx1==idx2:
            yo=(b-a+1)
        else:
            yo=(b-a+1)/(idx2-idx1)
        print('{0:.6f}'.format(1/yo,))
