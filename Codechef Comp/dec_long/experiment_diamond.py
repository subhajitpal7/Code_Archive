def test():
    n=int(input())
    arr=[]
    anssum=0
    for i in range(0,n):
        a=[]
        for j in range(0,n):
            a.append(i+j+2)
        arr.append(a)
    for a in arr:
        print(*a,sep=" ")
    print(anssum)
if __name__=="__main__":
    ans=[]
    anstemp=[]
    for i in range(1,int(input())+1):
        test()
