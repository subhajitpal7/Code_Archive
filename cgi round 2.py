from collections import Counter as cnt
from collections import defaultdict as dic
from random import randint
from time import time
def si():
    return input()
def ii():
    return int(si())
def mi():
    return map(int,si().split())
def sol2():
    cnt=0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]<arr[j]:
                for k in range(j+1,n):
                    if arr[j]>arr[k]:
                        cnt+=1
    print(cnt)
def sol1():
    store=dic()
    for i in range(1,n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                if i in store:
                    store[i]+=1
                else:
                    store[i]=1
    cnt=0
    #print(store)
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]<arr[j]:
                #print(arr[i],arr[j])
                if j in store:
                    cnt+=store[j]
    print(cnt)
if __name__=="__main__":
    for i in range(10):
        n=randint(pow(10,3),pow(10,4)+1)
        arr=[]
        for i in range(n):
            arr.append(randint(1,pow(10,6)))
        #n=ii()
        #arr=list(mi())
        s=time()
        sol1()
        e=time()
        print("op",e-s)
        #s=time()
        #sol2()
        #e=time()
    
