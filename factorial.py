def seive():
    for i in range(1,101):
        fact.append(fact[i-1]*i)
def fun():
    return fact[int(input())]
if __name__=="__main__":
    ans=[]
    fact=[1]
    seive()
    for _ in range(int(input())):
        ans.append(fun())
    print(*ans,sep="\n")
