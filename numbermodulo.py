def fun():
    a,x,m=map(int,input().split())
    if a>m:
        print(a%m)
    else:
        print(m%a)
if __name__=="__main__":
    for _ in range(int(input())):
        fun()
