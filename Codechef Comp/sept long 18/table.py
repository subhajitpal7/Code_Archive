'''0 L W L L
   W w w L L
   L L w w w
   W w L w L
w=2
L=0'''
from collections import defaultdict as dic
def si():
    return raw_input()
def ii():
    return int(si())
def mi():
    return map(int,si().split())
def sol():
    m=si()
    n=si()
    ln,lm=len(n),len(m)
    l=[]
    l=[[0]*(lm+1) for i in xrange(ln+1)]
    #print l
    mapper=dic()
    mapper[1]='W'
    mapper[2]='w'
    mapper[0]='L'
    qry=[]
    q=ii()
    for i in xrange(q):
        qry.append(list(mi()))
    for i in xrange(1,ln+1):
        if n[i-1]=='1':
            l[i][0]=0
        else:
            l[i][0]=1
    for i in xrange(1,lm+1):
        if m[i-1]=='1':
            l[0][i]=0
        else:
            l[0][i]=1
    for i in xrange(ln+1):
        for j in xrange(lm+1):
            print mapper[l[i][j]],
        print 
    print 'hula'
    for i in xrange(1,ln+1):
        a=max(l[i][0],l[i-1][1])
        if a==0:
            if l[i][0] or l[i-1][1]:
                l[i][1]=0
            else:
                l[i][1]=2
        elif a==1:
            l[i][1]=2
        elif a==2:
            if l[i][0]:
                l[i][1]=2
            else:
                l[i][1]=0
    for i in xrange(1,lm+1):
        a=max(l[0][i],l[1],i-1)
        if a==0:
            if l[0][i] or l[1][i-1]:
                l[1][i]=0
            else:
                l[1][i]=2
        elif a==1:
            l[1][i]=2
        elif a==2:
            if l[0][i]==1:
                l[1][i]=2
            else:
                l[1][i]=0
    for i in xrange(2,ln+1):
        for j in xrange(2,lm+1):
            a=min(l[i-1][j],l[i][j-1])
            if a:
                l[i][j]=0
            else:
                l[i][j]=2
    for i in xrange(ln+1):
        for j in xrange(lm+1):
            print mapper[l[i][j]],
        print 
if __name__=="__main__":
    for _ in xrange(ii()):
        sol()
  
