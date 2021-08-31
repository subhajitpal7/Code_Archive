def sol():
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    table=[999999999]*(n+1)
    table1=[-999999999]*(n+1)
    table[0]=0
    table1[0]=0
    for i in range(1,n+1):
        for j in range(k):
            if arr[j]<=i:
                sub_res=table[i-arr[j]]
                if sub_res!=999999999 and sub_res+1<table[i]:
                    table[i]=sub_res+1
            if arr[j]<=i:
                sub_res=table1[i-arr[j]]
                if sub_res!=-999999999 and sub_res+1>table1[i]:
                    table1[i]=sub_res+1
    if table[n]!=999999999:
        mincount=table[n]
    else:
        mincount=-1
    if table1[n]!=-999999999:
        maxcount=table1[n]
    else:
        maxcount=-1
    print(mincount,maxcount)
if __name__=="__main__":
    sol()
