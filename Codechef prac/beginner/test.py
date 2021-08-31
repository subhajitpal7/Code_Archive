#!/bin/python3

import sys
from bisect import bisect as bs
from random import randint as rd
from collections import defaultdict as dic
def simplestSum(k, a, b):
    store=[]
    pivot=[]
    store.append(1)
    pivot.append(1)
    sum1=1
    ans=0
    while sum1<b:
        sum1*=k
        sum1+=1
        pivot.append(sum1)
        store.append(pivot[-1]+store[-1])
    #print(pivot)
    #print(store)
    try:
        idx1=pivot.index(a)
    except Exception:
        idx1=bs(pivot,a)
        #ans+=store[idx1-1]*(pivot[idx1]-a)
    idx2=bs(pivot,b)-1
    #print(idx1,idx2)
    decision=0
    index=dic()
    for j in range(idx1,idx2+1):
        if pivot[j] in range(a,b+1):
            index[pivot[j]]=store[j]
    index[a]=store[idx1 if idx1==0 else idx1-1]
    index[b]=store[idx2]
    #print(index)
    
    '''for i in range(idx1+1,idx2+1):
        decision=1
        ans+=(store[i-1])*(pivot[i]-pivot[i-1])
        
    # Complete this function
    if decision==1:
        ans+=(store[idx2])*(b-pivot[idx2]+1)
    else:
        print("yeah")
        ans=(store[idx2-1])*(b-a+1)'''
    l=sorted(index.keys())
    #print(l)
    n=len(l)
    for y in range(1,n):
        ans+=(l[y]-l[y-1])*index[l[y-1]]
    ans+=(b-l[-1]+1)*index[l[-1]]
    return ans%mod
def fun(k,n):
    sum1=0
    i=1
    while i<n+1:
        sum1+=i
        i=i*k
        i+=1
    return sum1
if __name__ == "__main__":
    q = int(input().strip())
    mod=pow(10,9)+7
    for a0 in range(q):
        k, a, b = input().strip().split(' ')
        k, a, b = [int(k), int(a), int(b)]
        #k=rd(2,10000)
        #a=rd(1,3000000)
        #b=rd(a,3000000)
        print(k,a,b)
        result = simplestSum(k, a, b)
        ans=0
        for i in range(a,b+1):
            ans+=fun(k,i)
        #print("Actual sol,",ans%mod)
        #print("mysol",result)
        if ans%mod == result:
            print(True)
        else:
            print(False)
