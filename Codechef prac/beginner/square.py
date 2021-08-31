def sol():
    n=int(input())
    r=int(pow(n,.5))
    if n%r==0:
        print(2*(r+n//r))
    else:
        print((2*(r+n//r)-n%r)+(n%r + 2))
if __name__=="__main__":
    sol()
