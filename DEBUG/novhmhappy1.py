from bisect import bisect as bs
from random import randint
from random import shuffle
def si():
    return raw_input()
def ii():
    return int(si())
def mi():
    return map(int,si().split())
def sol2():
    #n,q,k=mi()
    #arr=list(mi())
    #s=si()
    shifts=s.count('!')+1
    l=[0]*(shifts)
    for i in xrange(shifts):
        max1=0
        #k=0
        temp=0
        for j in xrange(n):
            #print arr[(j-i)%n],
            if arr[(j-i)%n]:
                temp+=1
            else:
                if max1<temp:
                    max1=temp
                if max1>=k:
                    max1=k
                    break
                temp=0
        else:
            if max1<temp:
                max1=temp
            if max1>=k:
                max1=k
        #print
        l[i]=max1
    idx=0
    for a in s:
        if a=="!":
            idx=(idx+1)%n
        else:
            print "actualsol",l[idx]
    #print contseg
def sol1():
    #n,q,k=mi()
    #arr=list(mi())
    #s=si()
    contseg=[]
    starting=[]
    i,j=0,0
    while i<n and j<n:
        j=i
        while i<n and arr[i]==1:
            i+=1
        if j!=i:
            starting.append(j)
            contseg.append([j,i])
        i+=1
    l=len(contseg)
    mainidx=0
    for a in s:
        if a=="!":
            mainidx=(mainidx-1)%n
        else:
            idx=bs(starting,mainidx)
            if idx>=l:
                idx-=1
            #print idx
            max1=0
            for j in xrange(l):
                if starting[(idx+j)%l]>=mainidx:
                    temp=contseg[(idx+j)%l][0]
                else:
                    temp=mainidx
                diff=contseg[(idx+j)%l][1]-temp
                #print "1st",contseg[(idx+j)%l][1],temp
                if diff>=k:
                    diff=k
                elif (idx+j)%l==l-1 and mainidx:
                    idx+=1
                    #print "inside elif mainidx",mainidx
                    diff+=mainidx-contseg[(idx+j)%l][0]
                    if diff>=k:
                        diff=k
                    idx-=1
                if max1<diff:
                    max1=diff
                if max1==k:
                    break
            print "derived",max1
                
    #print contseg
    
if __name__=="__main__":
    maxn=pow(10,5)+5
    for _ in xrange(ii()):
        n=randint(1,10)
        q=randint(1,10)
        k=randint(1,10)
        minus=randint(1,n)
        arr=[0]*minus+[1]*(n-minus)
        shuffle(arr)
        minus=randint(1,q)
        s=['!']*minus+['?']*(q-minus)
        shuffle(s)
        print n,q,k
        print arr
        print s
        sol1()
        sol2()
                
            
            
         
            
