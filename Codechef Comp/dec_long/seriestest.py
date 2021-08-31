ans=[]
for i in range(int(input())):
    b=str(i)
    if len(b)==1:
        print(int(b))
    else:
        evencount=0
        oddcount=0
        for l in b:
            if int(l)%2==0:
                evencount+=int(1)
            else:
                oddcount+=int(l)
        ans.append(abs(evencount-oddcount))
print(*ans,sep=" ")
