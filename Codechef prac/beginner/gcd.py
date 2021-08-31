from functools import reduce
from collections import defaultdict as dic
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def sol():
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    if n==1:
        if arr[0]%k==0:
            print(1)
        else:
            print(0)
    else:
        temp=dic()
        flag=0
        for a in arr:
            if a%k==0:
                if a//k in temp:
                    temp[a//k]+=1
                else:
                    temp[a//k]=1
                if a==k:
                    flag=1
        l=sorted(temp.keys())
        m=len(l)
        if m==1:
            print(1)
        elif flag==1:
            print(m)
        else:
            i=0
            res=reduce(lambda x,y : gcd(x,y), l)
            while res!=1 and i<m:
                
                res=reduce(lambda x,y : gcd(x,y), l[i:])
                i+=1
            ans=0
            for j in range(i,m):
                ans+=temp[l[j]]
            print(1 if ans==0 else ans)
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
            
