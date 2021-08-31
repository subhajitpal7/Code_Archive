from math import sqrt
def sol():
    n=int(input())
    centre=list(map(int,input().split()))
    radii=list(map(int,input().split()))
    flist=[]
    for i in range(n):
        flist.append([centre[i],radii[i]])
    flist.sort(key= lambda x:x[0])
    temp=0
    for i in range(n-1):
        if flist[i][0]+flist[i][1]>=flist[i+1][0]-flist[i+1][1]:
            segment=(flist[i][1]+flist[i+1][1])-abs(flist[i][0]-flist[i+1][0])
            base=flist[i][1]-segment/2
            height=sqrt(pow(flist[i][1],2)-pow(base,2))
            if height>temp:
                temp=height
    print(temp)
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
