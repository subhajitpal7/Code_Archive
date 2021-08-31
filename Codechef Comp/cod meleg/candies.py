def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def sol():
    a,b=map(int,input().split())
    print(2*gcd(a,b))
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
    
