t=int(input())
for i in range(t):
    n=int(input())
    n=str(bin(n)[2:])
    l=len(n)
    ans=0
    for i in range(l):
        for j in range(i+1,l):
            if n[i]=='1':
                if n[j]=='1':
                    ans+=3
                else:
                    ans+=2
            else:
                if n[j]=='1':
                    ans+=1
    print(ans)   
