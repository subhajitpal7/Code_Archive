from bisect import bisect as bs
def sol():
    n,k=map(int,input().split())
    arr=sorted(map(int,input().split()))
    idx=bs(arr,k)
    temp=0
    for i in range(idx):
        for j in range(i+1,idx):
            if arr[i]+arr[j]<k:
                temp+=1
    return temp
if __name__=="__main__":
    print(sol())
    
    
