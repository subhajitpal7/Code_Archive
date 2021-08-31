
def factors(n):    
        l1, l2 = [], []
        for i in range(1, int(n ** 0.5) + 1):
            q,r = n//i, n%i     # Alter: divmod() fn can be used.
            if r == 0:
                l1.append(i) 
                l2.append(q)    # q's obtained are decreasing.
        if l1[-1] == l2[-1]:    # To avoid duplication of the possible factor sqrt(n)
            l1.pop()
        l2.reverse()
        return l1 + l2
if __name__=="__main__":
    for _ in range(int(input())):
        n,a,b,c=map(int,input().split())
        l=factors(n)
        ans=0
        for i in l:
            if i<=a:
                p=n//i
                for j in l:
                    if p%j==0 and j<=b:
                        if p//j<=c:
                            ans+=1
        print(ans)
