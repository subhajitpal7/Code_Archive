n=int(input())
s=set(map(int,input().split()))
s=list(s)
revenue=set()
for i in range(len(s)):
    for j in range(i+1,len(s)):
        revenue.add(abs(s[i-1]-s[j-1]))
revenue=list(revenue)
mul=((n*(n-1))//2)//len(revenue)
ans=0
for i in revenue:
    ans+=i*mul
print(ans)
