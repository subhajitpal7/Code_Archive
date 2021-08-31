def sol():
    M,N=map(int,input().split())
    rx,ry=map(int,input().split())
    n=int(input())
    s=input()
    x,y=0,0
    for a in s:
        if a=='L':
            x-=1
        elif a=='R':
            x+=1
        elif a=='U':
            y+=1
        elif a=='D':
            y-=1
    if x==rx and y==ry:
        return "REACHED"
    elif (x in range(0,M+1)) and (y in range(0,N+1)):
        return "SOMEWHERE"
    else:
        return "DANGER"
if __name__=="__main__":
    for i in range(int(input())):
        print("Case "+str(i+1)+": "+sol())
