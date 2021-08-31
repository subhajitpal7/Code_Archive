def ii():
    return int(input())
def mi():
    return map(int,input().split())
def sol():
    n,m=mi()
    need=list(mi())[:n]
    if n==0 or m==0:
        print(0,0)
        return
    alloc=sorted(mi())[:m]
    alloc=alloc[::-1]
    count=0
    temp=999999
    bcount=0
    for i in range(n):
        for j in range(m):
            if need[i]%alloc[j]==0 and temp>(need[i]//alloc[j]):
                temp=(need[i]//alloc[j])
                break
        if temp!=999999:
            bcount+=temp
            count+=1
        temp=999999
    print(count,bcount)
if __name__=="__main__":
	for _ in range(ii()):
		sol()
