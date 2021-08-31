def sol():
    n=int(input())
    arr=list(map(int,input().split()))
    chef1=[]
    chef2=[]
    chef1_count=0
    chef2_count=0
    for i in range(n):
        if i%2==0:
            chef1.append(arr[i])
        else:
            chef2.append(arr[i])
    chef1.sort(reverse=True)
    chef2.sort(reverse=True)
    for i in range(n//2):
        if chef1[i]>chef2[i]:
            chef1_count+=1
        else:
            chef2_count+=1
    if chef1_count>chef2_count:
        print("1")
    elif chef1_count==chef2_count:
        print("draw")
    else:
        print("2")
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
