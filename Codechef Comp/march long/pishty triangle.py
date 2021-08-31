def sol():
    n,q=map(int,input().split())
    A=list(map(int,input().split()))
    for i in range(q):
        dec,a,b=map(int,input().split())
        if dec==1:
            A[a-1]=b
            #print(A)
        else:
            temp=0
            B=A[a-1:b]
            B.sort(reverse=True)
            #print(B)
            for i in range(b-a-1):
                if (B[i]+B[i+2])>B[i+1] and (B[i]+B[i+1])>B[i+2] and (B[i+2]+B[i+1])>B[i]:
                    temp=B[i]+B[i+1]+B[i+2]
                    break
            print(temp)
if __name__=="__main__":
    sol()
                
