def rainbow():
    n=int(input())
    a=list(map(int,input().split()))[:n]
    if a[n//2]==7:
           b=a[:n//2]
           c=a[n//2+1:]
           c=c[::-1]
           if c==b:
                return "yes"
           else:
                return "no"
    else:
           return "no"
if __name__=="__main__":
           ans=[]
           for _ in range(int(input())):
                ans.append(rainbow())
           print(*ans,sep="\n")
    
