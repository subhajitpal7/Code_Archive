from collections import Counter as cnt
def sol():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    #a=[rd(1,10) for i in range(n)]
    #print(a)
    temp=cnt(a)
    l=list(temp.keys())
    b=len(l)
    ans=0
    for i in range(b):
        for j in range(i,b):
            if abs(l[i]-l[j])>=k:
                ans+=(temp[l[i]]*temp[l[j]])
    print(ans)
if __name__=="__main__":
    sol()
