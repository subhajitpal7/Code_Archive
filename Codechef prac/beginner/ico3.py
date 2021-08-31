def maxSumWO3Consec(arr, n):
    if n<3:
        return sum(arr)
    sum1 = [0 for k in range(n)]
    sum1[0] = arr[0]
    sum1[1] = arr[0] + arr[1]
    sum1[2] = max(sum1[1], max(arr[1] + arr[2], arr[0] + arr[2]))
    for i in range(3,n):
        sum1[i] = max(max(sum1[i-1], sum1[i-2] + arr[i]),arr[i] + arr[i-1] + sum1[i-3])
    return sum1[n-1]
n=int(input())
arr = list(map(int,input().split()))
print(maxSumWO3Consec(arr, n))
