def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors
pfs = prime_factors(24)
largest_prime_factor = max(pfs)
print(pfs)
