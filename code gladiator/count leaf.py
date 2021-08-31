from collections import defaultdict as dic
def delnode(a):
    if treelist[a]!=[]:
        for i in range(len(treelist[a])):
            delnode(treelist[a][i])
    else:
        del(treelist[a])
def sol():
    n=int(input())
    trees=list(map(int,input().split()))
    node=int(input())
    for i in range(n):
        treelist[i]=[]
    for i in range(n):
        if trees[i]>-1:
            treelist[trees[i]].append(i)
    leafcount=0
    delnode(node)
    for a in treelist:
        if treelist[a]==[]:
            leafcount+=1
    print(leafcount)
if __name__=="__main__":
    treelist=dic()
    sol()
