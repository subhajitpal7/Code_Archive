def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.add(i)
    return i
def historic(n):
    primes = set([2])
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return primes
        i += 1
primes=sorted(historic(10000))
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primes[n-1])
