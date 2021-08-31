def fun():
    days=[0]*7
    n,m=map(str,input().split())
    n=int(n)
    k=0
    if m=='mon':
        k=0
    elif m=='tues':
        k=1
    elif m=='wed':
        k=2
    elif m=='thurs':
        k=3
    elif m=='fri':
        k=4
    elif m=='sat':
        k=5
    elif m=='sun':
        k=6
    for i in range(0,n):
        days[(k+i)%7]+=1
    print(*days)
if __name__=="__main__":
    for i in range(int(input())):
        fun()
