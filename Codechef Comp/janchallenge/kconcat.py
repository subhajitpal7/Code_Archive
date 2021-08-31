def maxSubArraySum(a,size,k):
    max_so_far =a[0]
    curr_max = a[0]
    for i in range(1,size*k):
        curr_max = max(a[i%size], curr_max + a[i%size])
        max_so_far = max(max_so_far,curr_max)  
    return max_so_far
def solve():
    length,k=map(int,input().split())
    arr=list(map(int,input().split()))[:length]
    sum1=sum(arr)
    if sum1>0:
        maxsum=0
        n=length
        maxsum1=maxSubArraySum(arr,n,1)
        maxsum2=maxSubArraySum(arr,n,2)
        diff=maxsum2-maxsum1
        print(maxsum1+(diff*(k-1)))
    else:
        maxsum=0
        n=length
        maxsum1=maxSubArraySum(arr,n,1)
        maxsum2=maxSubArraySum(arr,n,2)
        diff=maxsum2-maxsum1
        print(maxsum1+(diff*(k-1)))
if __name__=="__main__":
    for _ in range(int(input())):
        solve()
    
