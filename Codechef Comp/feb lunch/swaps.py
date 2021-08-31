def updateindex(index,a,ai,b,bi):
 
    index[a] = ai
    index[b] = bi
def minSwapsUtil(arr,pairs,index,i,n):
    if (i > n):
        return 0
    if (pairs[arr[i]] == arr[i+1]):
         return minSwapsUtil(arr, pairs, index, i+2, n)
    one = arr[i+1]
    indextwo = i+1
    indexone = index[pairs[arr[i]]]
    two = arr[index[pairs[arr[i]]]]
    arr[i+1],arr[indexone]=arr[indexone],arr[i+1]
    updateindex(index, one, indexone, two, indextwo)
    a = minSwapsUtil(arr, pairs, index, i+2, n)
    arr[i+1],arr[indexone]=arr[indexone],arr[i+1]
    updateindex(index, one, indextwo, two, indexone)
    one = arr[i]
    indexone = index[pairs[arr[i+1]]]
    two = arr[index[pairs[arr[i+1]]]]
    indextwo = i
    arr[i],arr[indexone]=arr[indexone],arr[i]
    updateindex(index, one, indexone, two, indextwo)
    b = minSwapsUtil(arr, pairs, index, i+2, n)
    arr[i],arr[indexone]=arr[indexone],arr[i]
    updateindex(index, one, indextwo, two, indexone)
    return 1+min(a, b)
def minSwaps(n,pairs,arr):
    index=[]
    for i in range(2*n+1+1):
        index.append(0)
    for i in range(1,2*n+1):
        index[arr[i]]=i
    return minSwapsUtil(arr, pairs, index, 1, 2*n)
#arr = [0, 3, 5, 6, 4, 1, 2]
#pairs= [0, 3, 6, 1, 5, 4, 2]
#m = len(pairs)
#n = m//2
#print("Min swaps required is ",minSwaps(n, pairs, arr))
if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int,input().split()))
        dec1=False
        for i in range(2*n+1):
            dec1=False
            if arr[i%2*n]!=arr[(i+1)%2*n]:
                dec1=True
            
        if not dec1:
            print(0)
        else:
            arr.insert(0,0)
            pairs=[0]
            for i in range(n):
                pairs.append(i+1)
                pairs.append(i+1)
            #print(arr)
            #print(pairs)
            print(minSwaps(n,pairs,arr))
