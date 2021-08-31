from bisect import bisect as b
def solve():
    n=int(input())
    A=[]
    for i in range(n):
        a=sorted(list(set(map(int,input().split()))))
        A.append(a)
    sum1=A[n-1][len(A[n-1])-1]
    idx=1
    pickup=[A[n-1][len(A[n-1])-1]]
    for i in range(n-1,0,-1):
        if A[i-1][0]>=pickup[-1]:
            print(-1)
            break
        else:
            idx=b(A[i-1],pickup[-1])
            while True:
                if pickup[-1]==A[i-1][idx-1]:
                    idx-=1
                else:
                    break
            sum1+=A[i-1][idx-1]
            pickup.append(A[i-1][idx-1])
            k=idx-1
    else:
        print(sum1)
if __name__=="__main__":
    for _ in range(int(input())):
        solve()
