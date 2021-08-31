def test():
    n=int(input())
    arr=[]
    anssum=0
    for i in range(0,n):
        a=[]
        for j in range(0,n):
            b=str(i+j+2)
            if len(b)==1:
                a.append(int(b))
                anssum+=int(b)
            else:
                evencount=0
                oddcount=0
                for l in b:
                    if int(l)%2==0:
                        evencount+=int(1)
                    else:
                        oddcount+=int(l)
                a.append(abs(evencount-oddcount))
                anssum+=abs(evencount-oddcount)
        arr.append(a)
    for a in arr:
        print(*a,sep=" ")
    print(anssum)
if __name__=="__main__":
    ans=[]
    anstemp=[]
    for i in range(1,int(input())+1):
        ans.append(test())
    print(*ans,sep=" ")
    '''for i in range(len(ans)-1):
        anstemp.append(ans[i+1]-ans[i])
    print(*anstemp,sep=" ")'''
