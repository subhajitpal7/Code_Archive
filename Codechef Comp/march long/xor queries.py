def sol():
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    temp=max(arr)
    length=len(bin(temp)[2:])
    counts=[]
    for i in range(n):
        s=bin(arr[i])[2:].rjust(length,'0')
        if i==0:
            temp=[]
            for a in s:
                count1=0
                count0=0
                if a=='1':
                    count1=1
                else:
                    count0=1
                temp.append([count0,count1])
            counts.append(temp)
        else:
            temp=[]
            for j in range(length):
                count1=0
                count0=0
                if s[j]=='1':
                    count1=1
                else:
                    count0=1
                temp.append([counts[i-1][j][0]+count0,counts[i-1][j][1]+count1])
            counts.append(temp)
    for i in range(q):
        ans='1'*(31-length)
        l,r=map(int,input().split())
        val=False
        if l==1:
            val=True
        for j in range(length):
            if not val:
                count1=counts[r-1][j][1]-counts[l-2][j][1]
                count0=counts[r-1][j][0]-counts[l-2][j][0]
            else:
                count1=counts[r-1][j][1]
                count0=counts[r-1][j][0]
            if count1<count0:
                ans+='1'
            else:
                ans+='0'
        print(int(ans,2))
if __name__=="__main__":
    sol()
