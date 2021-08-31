from math import sqrt
from math import floor
def sol():
    n=int(input())
    #print(close_triangle(n))
    if n==1:
        print(1)
    else:
        m=floor(sqrt(2*n))
        t1=m*(m+1)//2
        flag=False
        while t1<n:
            flag=True
            t1=m*(m+1)//2
            m+=1
        if flag==False:
            l=m-1
        else:
            l=m-2
        t2=l*(l+1)//2
        if n==t1:
            print(m)
        elif n==t2:
            print(l)
        elif t1-n>n-t2:
            print(l+n-t2)
        elif n-t2>t1-n:
            print(m+t1-n)
        elif n-t2==t1-n:
            print(l+t1-n)
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
