import functools
from operator import mul
n=int(input())
arr=list(map(int,input().split()))[:n]
for _ in range(int(input())):
    a=list(map(int,input().split()))
    if a[0]==1:
        i,j,x=a[1],a[2],a[3]
        for k in range(i-1,j):
            arr[k]=x
    elif a[0]==2:
        i,j,k,l,m=a[1],a[2],a[3],a[4],a[5]
        p1=arr[i-1:j]
        p2=arr[k-1:l]
        result1=1
        result2=1
        for item in p1:
            result1*=item
        for item in p2:
            result2*=item
        if result1%result2==0:
            print((result1//result2)%m)
        else:
            print(-1)
