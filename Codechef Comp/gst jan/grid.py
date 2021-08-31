def grid():
    arr=list(map(int,input().split()))
    t=arr[0]
    arr=arr[1:]
    if t in arr:
        return "YES"
    else:
        return "NO"
if __name__=="__main__":
    for _ in range(int(input())):
        print(grid())
