def fun():
    n=int(input())
    actual=[]
    time=[5,15,30,60]
    for i in range(n):
        val=0
        a=list(map(str,input().split()))
        if int(a[3]) in time:
            arr=[int(a[0]),int(a[1]),int(a[2]),int(a[3]),a[4],a[5],i]
            if(len(actual)==0):
                print("wait")
            else:
                for a in actual:
                    if (arr[0] in range(a[1],a[2]+1)) and (a[0] in range(arr[1],arr[2]+1)) and (arr[3]==a[3]) and (a[4]==arr[4]) and((arr[5]=='white' and a[5]=="black") or (arr[5]=='black' and a[5]=="white") or (arr[5]=='random' and a[5]=='random')):
                        print(a[6]+1)
                        actual.remove(a)
                        val=1
                        break
                if val==0:
                    print("wait")
            if val==0:
                actual.append(arr)
if __name__=="__main__":
    for _ in range(int(input())):
        fun()
