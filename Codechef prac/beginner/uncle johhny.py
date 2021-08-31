def sol():
    n=int(input())
    arr=list(map(int,input().split()))
    idx=int(input())-1
    temp=arr[idx]
    print(sorted(arr).index(temp)+1)
if __name__=="__main__":
    for _ in range(int(input())):
        sol()

	
