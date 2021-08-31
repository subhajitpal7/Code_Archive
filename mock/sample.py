def si():
    return raw_input()
def ii():
    return int(si())
def mi():
    return map(int,si().split(','))
def csb(n):
    c = 0
    while (n):
        n &= (n-1) 
        c+=1
    return c
def sol():
    n=ii()
    arr=list(mi())
    b=[]
    ans=0
    for a in arr:
        b.append(csb(a))
    for i in xrange(n-1):
        for j in xrange(i+1,n):
            if b[i]>b[j]:
                ans+=1
    print ans
if __name__=="__main__":
    sol()
