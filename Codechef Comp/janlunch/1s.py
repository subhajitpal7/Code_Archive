def sol():
    n=int(input())
    arr=sorted(map(int,input().split()))
    if sum(arr)%2==0:
        print(1)
    else:
        print(len(arr) if len(arr)<2 else 2)
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
