from collections import defaultdict as dic
def sol():
    n=int(input())
    arr=list(map(int,input().split()))
    arr.append(arr[0])
    pick=[0]*(n+1)
    sum1=0
    for i in range(n):
        if arr[i]<arr[i+1] and pick[i]==0:
            sum1+=arr[i]
            pick[i]=1
            if i==0:
                pick[n]=1
        elif arr[i]>=arr[i+1] and pick[i+1]==0:
            sum1+=arr[i+1]
            pick[i+1]=1
    return sum1
if __name__=="__main__":
    print(sol())
    
    
