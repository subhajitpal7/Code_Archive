def sol():
    n=int(input())
    arr=list(map(int,input().split()))
    temp=0
    for i in range(0,n,3):
        temp+=(min(arr[i:i+3]))
    return temp
if __name__=="__main__":
    print(sol())
    
    
