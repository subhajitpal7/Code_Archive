def maxSubArraySum(a,n,l):      
    max_so_far = -100000000000
    max_ending_here = 0
    for i in range(0, n*l):
        max_ending_here = max_ending_here + a[i%n]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0  
    return max_so_far
if __name__=="__main__":
    for _ in range(int(input())):
        n,k=map(int,input().split())
        arr=list(map(int,input().split()))
        if n*k<=10**5:
            maxsum=0
            maxsum1=maxSubArraySum(arr,n,1)
            maxsum2=maxSubArraySum(arr,n,2)
            diff=maxsum2-maxsum1
            print(maxsum1+(diff*(k-1)))
        else:
            maxsum=0
            maxsum1=maxSubArraySum(arr,n,1)
            maxsum2=maxSubArraySum(arr,n,2)
            maxsum3=maxSubArraySum(arr,n,3)
            diff=maxsum2-maxsum1
            diff1=maxsum3-maxsum2
            if diff1==0 and k>1:
                print(maxsum2)
            elif diff==0 and k==1:
                print(maxsum1)
            else:
                print(maxsum2+(diff1*(k-2)))
