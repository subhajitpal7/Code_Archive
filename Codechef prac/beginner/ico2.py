def sol():
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    temp=0
    for i in range(n):
        for j in range(i+1,n):
            if abs(arr[i]-arr[j])>=k:
                temp+=1
    return temp
if __name__=="__main__":
    print(sol())
