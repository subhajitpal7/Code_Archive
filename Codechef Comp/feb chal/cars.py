def fun():
    n=int(input())
    process=list(map(int,input().split()))
    c,d,s=map(int,input().split())
    print((c-1)*max(process))
if __name__=="__main__":
    for _ in range(int(input())):
        fun()
