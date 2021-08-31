import sys,bisect
def fibo(n):
    return int(fibcons1*(fibcons2**n+fibcons3**n))
cons=5**.5
fibcons1=1/cons
fibcons2=(1+cons)/2
fibcons3=(cons-1)/2
store=[]
storesum=[0 for i in range(33)]
k=0
storesum[k]=0
for i in range(85):
    temp=int(fibcons1*(fibcons2**i+fibcons3**i))
    if temp%2==0:
        store.append(temp)
        k+=1
        storesum[k]=storesum[k-1]+temp
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    idx=bisect.bisect(store,n)
    print(sum(store[:idx]))
