t=int(input())
for i in range(t):
    k,a,b=map(int,input().split())
    c=(a+b)%10
    k-=2
    ans=a+b
    zero=False
    while(k>0):
        if c==0:
            zero=True
            break
 
        elif c!=2:
            k-=1
            ans+=c
            c=(c*2)%10
        elif c==2:
            break
    x=k//4
    y=k%4
    common=2+4+8+6
    if zero==False:
        ans+=common*x
        while(y>0):
            #print c
            ans+=c
            y-=1
            c=(c*2)%10
    #print ans
    if ans%3==0:
        print('YES')
    else:
        print('NO') 
