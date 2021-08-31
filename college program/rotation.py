def sol():
    n=int(input())
    arr=[]
    arr90=[[0 for i in range(n)] for i in range(n)]
    arr180=[[0 for i in range(n)] for i in range(n)]
    arr270=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        a=list(map(int,input().split()))
        arr.append(a)
    #90 rotation
    a=0
    b=0
    for i in range(n):
        b=0
        for j in range(n-1,-1,-1):
            arr90[a][b]=arr[j][i]
            b+=1
        a+=1
    #180 rotation
    a,b=0,0
    for i in range(n):
        b=0
        for j in range(n-1,-1,-1):
            arr180[a][b]=arr90[j][i]
            b+=1
        a+=1
    #270 rotation
    a,b=0,0
    for i in range(n):
        b=0
        for j in range(n-1,-1,-1):
            arr270[a][b]=arr180[j][i]
            b+=1
        a+=1
    rotate=0
    while True:
        c=input().split()
        if c[0]=='-1':
            break
        elif c[0]=='A':
            rotate=(rotate+int(c[1]))%360
        elif c[0]=='Q':
            k,l=int(c[1])-1,int(c[2])-1
            if rotate==0:
                print(arr[k][l])
            elif rotate==90:
                print(arr90[k][l])
            elif rotate==180:
                print(arr180[k][l])
            elif rotate==270:
                print(arr270[k][l])
        elif c[0]=="U":
            k,l,u=int(c[1])-1,int(c[2])-1,int(c[3])
            arr[k][l]=u
            arr90[l][n-k-1]=u
            arr180[n-k-1][n-l-1]=u
            arr270[n-1-l][k]=u
if __name__=="__main__":
    sol()
