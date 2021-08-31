def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0]*M
    j = 0 
    computeLPSArray(pat, M, lps)
    i = 0
    anslist=[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
 
        if j == M:
            #print("Found pattern at index " + str(i-j))
            anslist.append(i-j)
            j = lps[j-1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return anslist
def computeLPSArray(pat, M, lps):
    len = 0
    lps[0]
    i = 1
    while i < M:
        if pat[i]==pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1
def sol():
    s=input()
    x=int(input())
    f=input()
    l=len(f)
    ans=KMPSearch(f,s)
    t=len(ans)
    reformedans=set()
    for i in range(t-1):
        if ans[i]+l<ans[i+1]:
            reformedans.add(ans[i])
            reformedans.add(ans[i+1])
    reformedans=sorted(reformedans)
    #print(reformedans)
    if len(reformedans)>=2:
        if reformedans[0]%x!=0:
            first=reformedans[0]//x+1
        else:
            first=reformedans[0]//x
        if ans[-1]%x!=0:
            second=reformedans[-1]//x+1
        else:
            second=reformedans[-1]//x
        print(first,second if first!=second else -1)
    else:
        print(-1)
        
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
