def edit_distance():
    s,t=input(),input()
    len1,len2=len(s),len(t)
    D=[[0]*(len2+1) for i in range(len1+1)]
    for i in range(len1+1):
        D[i][0]=i
    for j in range(len2+1):
        D[0][j]=j
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if s[i-1]==t[j-1]:
                D[i][j]=D[i-1][j-1]
            else:
                D[i][j]=min(D[i][j-1],D[i-1][j],D[i-1][j-1])+1
    return D[i][j]
if __name__=="__main__":
    ans=[]
    for _ in range(int(input())):
        ans.append(edit_distance())
    print(*ans,sep="\n")
