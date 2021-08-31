def si():
    return raw_input()
def ii():
    return int(si())
def mi(fun):
    return map(fun,si().split())
def sol():
    n=ii()
    arr=list(mi(int))
    prefix=[0]*n
    suffix=[0]*n
    prefix[0]=arr[0]
    for i in xrange(1,n):
        prefix[i]=max(arr[i],prefix[i-1])
    suffix[-1]=arr[-1]
    for i in xrange(n-2,-1,-1):
        suffix[i]=min(arr[i],suffix[i+1])
    goodlen=1
    i,j=0,0
    while j<n and i<n:
        if prefix[i]>=suffix[j]:
            goodlen=max(goodlen,j-i+1)
            j+=1
        else:
            i+=1
    print goodlen
        
if __name__=="__main__":
    for i in xrange(ii()):
        sol()
