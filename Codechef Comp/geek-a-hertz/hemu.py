def classatten():
    n=int(input())
    s=[]
    ans=0
    for i in range(n):
        b=input()
        if b in s:
            s.remove(b)
            ans-=1
        else:
            s.append(b)
            ans+=1
    print(ans)
if __name__=="__main__":
    for _ in range(int(input())):
        classatten()
    
