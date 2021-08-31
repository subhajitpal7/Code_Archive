from collections import defaultdict as dic
def fac(num):
    if num < 0:
        raise ValueError("Negative numbers have no factorial.")
    else:
        if num in facts:
            return facts[num]
        else:
            for i in range(max(facts)+1,num+1):
                facts[i]=facts[i-1]*i
            return facts[num]
def binom(x, y):
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom
def sol():
    n=int(input())
    ans=0
    limit=n//2
    for i in range(n//2+1):
        ans+=binom(n,i)-binom(n-i,i)
    print(ans%mod)
if __name__=="__main__":
    facts=dic()
    facts[0]=1
    mod=pow(10,6)+3
    for i in range(int(input())):
        sol()
        
