from collections import defaultdict as dic
def fac(num):
    if num < 0:
        raise ValueError("null")
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
    val=ord('a')
    store=dic()
    temp=0
    for i in range(n):
        s=input()
        for a in s:
            temp+=ord(a)-val
        if temp in store:
            store[temp]+=1
        else:
            store[temp]=1
        temp=0
    ans=0
    for a in store:
        if store[a]>=2:
            ans+=binom(store[a],2)
    print(ans)
if __name__=="__main__":
    facts=dic()
    facts[0]=1
    sol()
