from functools import reduce
def GCD(a, b):

    if b == 0:
        return a
    else:
        return GCD(b, a % b)
def pythtrip():
    a,b,c=(map(int,input().split()))
    gcd = reduce(GCD, (a, b, c))
    if gcd==1:
        print("YES")
    else:
        print("NO")
if __name__=="__main__":
    for _ in range(int(input())):
        pythtrip()
    
        
