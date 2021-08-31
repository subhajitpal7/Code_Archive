def sol():
    n=int(input())
    arr=list(map(int,input().split()))
    count=n
    for i in range(n-1):
        if arr[i]<=arr[i+1]:
            count+=1
    print(count)
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
