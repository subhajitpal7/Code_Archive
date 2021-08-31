def ii():
    return int(input())
def mi():
    return map(int,input().split())
def si():
    return input()
def sol():
    n=ii()
    arr=[]
    for i in range(n):
        arr.append(list(mi()))
    q=ii()
    for i in range(q):
        l,r=mi()
        temp=arr[l-1:r]
        ans=0
        for a,b in temp:
            i+=1
            if i<n:
                for c,d in temp:
                    if (pow(a-c,2)+pow(b-d,2))>ans:
                        ans=(pow(a-c,2)+pow(b-d,2))
        #x1,y1=temp[0]
        #x2,y2=temp[-1]
        #print(pow(x2-x1,2)+pow(y2-y1,2))
        print(ans)
                    
if __name__=="__main__":
    sol()
