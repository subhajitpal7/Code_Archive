def sol():
    n=int(input())
    arr=list(map(int,input().split()))
    votes=[0 for i in range(n)]
    for i in range(n):
        temp=0
        for j in range(i+1,n):
            if arr[i]>=temp:
                votes[j]+=1
            else:
                break    
            temp+=arr[j]
        #print(arr[i],"->",votes)
            
    for i in range(n-1,-1,-1):
        temp=0
        for j in range(i-1,-1,-1):
            if arr[i]>=temp:
                votes[j]+=1
            else:
                break
            temp+=arr[j]
        #print(votes)
    print(*votes)
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
