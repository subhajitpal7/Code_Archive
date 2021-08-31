def sol():
    n=int(input())
    arr=sorted(map(int,input().split()))
    diff=abs(arr[0]-arr[1])
    for i in range(n-1):
        if abs(arr[i]-arr[i+1])<diff:
            diff=abs(arr[i]-arr[i+1])
    print(diff)
            
if __name__=="__main__":
    for _ in range(int(input())):
        sol()

	
