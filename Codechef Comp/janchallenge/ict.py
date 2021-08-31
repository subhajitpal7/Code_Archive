arr=list(map(int,input().split()))
n=len(arr)
arr=arr*2
n=n*2
maxsum=-100000000
for i in range(n-1):
    temp=[]
    k=i
    while True:
        if k+1<n and arr[k+1]>=arr[k]:
            temp.append(arr[k+1])
            k+=1
        else:
            #temp.append(arr[k])
            break
    g=sum(temp)
    if g>maxsum:
        maxsum=g
print(maxsum)
'''ansfinal=[]
lenans=0
for a in ans:
    if len(a)>lenans:
        lenans=len(a)
for a in ans:
    if len(a)==lenans:
        ansfinal.append(a)
if len(ansfinal)<1:
    print("NA")
else:
    for a in ansfinal:
        print(*a,sep=" ")'''
