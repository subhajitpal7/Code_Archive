def goodsubstr():
    s=input()
    count=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if abs(i-j)>2:
                if s[i]==s[j]:
                    b=s[i+1:j]
                    if b.count(b[0])==len(b):
                        count+=1
    return count
if __name__=="__main__":
    ans=[]
    for _ in range(int(input())):
        ans.append(goodsubstr())
    print(*ans,sep="\n")