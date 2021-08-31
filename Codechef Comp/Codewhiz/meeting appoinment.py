def fun():
    n=int(input())
    arr=list(map(int,input().split()))
    l=[]
    for i in range(n):
        temp=arr[i*2:(i+1)*2]
        l.append(temp)
    l=sorted(l)
    print(l)
if __name__=="__main__":
    for _ in range(int(input())):
        fun()
