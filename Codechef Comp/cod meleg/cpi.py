def sol():
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    temp=[]
    temp2=[]
    ans2=0
    ans1=0
    for i in range(n):
        if i<x:
            ans1+=(i+1)
            ans2+=(arr[i]*(i+1))
        temp.append([arr[i]/(i+1),i+1])
        temp2.append([arr[i]*(i+1),i+1])
    temp.sort(reverse=True)
    temp2.sort(reverse=True)
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    if x==1:
        print(max(arr))
        return
    for i in range(x):
        sum1+=arr[temp[i][1]-1]*(temp[i][1])
        sum2+=temp[i][1]
        sum3+=temp2[i][0]
        sum4+=temp2[i][1]
    print(max(sum1/sum2,sum3/sum4,ans2/ans1))
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
        
