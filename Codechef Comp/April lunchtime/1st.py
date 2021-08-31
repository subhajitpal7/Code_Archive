def ii():
    return int(input())
def mi():
    return map(int,input().split())
def si():
    return input()
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def lpf(n):
    d = 2
    temp=d
    while d*d <= n:
        while (n % d) == 0:
            if d>temp:
                temp=d# supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > temp:
        temp=n
    return temp
def sol():
    n,k=mi()
    if n==1:
        print("NO")
        return
    arr=list(mi())
    a=arr[0]
    for i in range(n-1):
        a=gcd(a,arr[i])
    #print(a)
    b=lpf(a)
    #print(b)
    if a==1:
        print("YES")
    elif b>k:
        print("NO")
    else:
        print("YES")
if __name__=="__main__":
    for _ in range(ii()):
        sol()
