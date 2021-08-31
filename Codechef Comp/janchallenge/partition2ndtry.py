def find_subset(S, sum1):
    n=len(S)
    ans=[]
    val=0
    for i in range(n-1,-1,-1):
        if sum1-S[i]>0:
            ans.append(S[i])
            sum1-=S[i]
        elif sum1-S[i]==0:
            sum1-=S[i]
            ans.append(S[i])
            val=1
            break
    if val==1:
        return ans
    else:
        return []
# main
if __name__ == "__main__":
    for _ in range(int(input())):
        x,n=map(int,input().split())
        sum1=(n*(n+1)//2)-x
        if sum1%2==0:
            ans=['']*n
            ans[x-1]='2'
            S=[i for i in range(1,n+1)]
            S.remove(x)
            sum_subset = find_subset(S,sum1//2)
            if len(sum_subset)==0:
                print("impossible")
            else:
                if 1 in sum_subset:
                    for a in sum_subset:
                        ans[a-1]='0'
                    for a in S:
                        if a not in sum_subset:
                            ans[a-1]='1'
                    print(''.join(ans))
                else:
                    for a in sum_subset:
                        ans[a-1]='1'
                    for a in S:
                        if a not in sum_subset:
                            ans[a-1]='0'
                    print(''.join(ans))
                    
        else:
            print("impossible")

