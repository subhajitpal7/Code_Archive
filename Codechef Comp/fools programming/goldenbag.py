def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
primes=get_primes(100000)
if __name__=="__main__":
    for _ in range(int(input())):
        b=int(input())
        for a in primes:
            if b-a in primes:
                print(a,b-a)
                break
    
