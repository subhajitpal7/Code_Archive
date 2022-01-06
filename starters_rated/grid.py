def si():
    return input()
def ii():
    return int(input())
def mi():
    return map(int,input().split())
def sol():
    N,x,y=mi()
    mid=(N+1)//2
    s = abs(mid-x)+abs(mid-y)
    if (x+y)%2==0:
        return 0
    else:
        return 1
if __name__=="__main__":
    for i in range(int(input())):
        print(sol())