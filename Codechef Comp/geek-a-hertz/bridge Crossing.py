def bridgetime():
    n=int(input())
    time=sorted(list(map(int,input().split())))[:n]
    return sum(time[1:])+(n-2)*time[0]
if __name__=="__main__":
    for _ in range(int(input())):
        print(bridgetime())
